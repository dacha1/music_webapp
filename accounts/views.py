from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

# Create your views here.


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already exist!')
                return render(request, 'signup.html')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email already exist!')
                return render(request, 'signup.html')
            else:
                user = User.objects.create_user(username=username, email=email, first_name=first_name,
                                                last_name=last_name,
                                                password=password1)
                user.save()
                messages.info(request, 'Sign up successfully!')
                return redirect('login')

        else:
            messages.info(request, 'Password mismatch!')
            return render(request, 'signup.html')

    else:
        return render(request, 'signup.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "Invalid username or password!")
            return render(request, 'signin.html')
    else:
        return render(request, 'signin.html')


def logout(request):
    auth.logout(request)
    return redirect('/')
