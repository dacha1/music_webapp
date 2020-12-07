# MUSIC WEBAPP
Webapp based on django
Music_webapp is a website that is used to promote the artists. This website gives the details information about the artists biography such as brief background, genre, their nationality, locations and about their albums. This app also provide social media information of the artists. I had used different programming language and tools such as Django framework, github for version control, python, postgres for database, pycharm, Html, CSS. As a user I am able to login or register using email id. I can view the home page with the list of artists. As I am the admin I can add, delete, edit, update artist records to an admin page. I can add albums to the website. I can add, remove, update adminor users. I I am also able to view artists social media account links, can see album of each artists. I can also able to visit youtube channel or soundcloud of each artists to listen to them.
In order to run this project in another laptop, following steps should be followed:
- Step 1- First download this project from the github.
- Step 2- Postgres can be installed on local machine through this link https://www.postgresql.org/download/. I have use postgres as database for this project.

**Note: I have use psycopg2==2.8.6 as postgres library for my window. For mac we have to use psycopg2-binary instead of psycopg2-binary. Use this command on terminal to install.** **pip install psycopg2-binary**
- Step 3 - Install pip install -r requirements.txt which installs all the dependencies required for the project.
- Step 4 - Download PG admin if not installed already.
- Step 5 - Run python manage.py makemigrations to create a migration, then run python manage.py migrate to create database tables.
- Step 6 - At last run the python manage.py runserver. It provides the link like 127.0.0.1:8000. Go to this link then the home page is available then sign up and login the webapp and can add the all the informations that i had provided in the top like add artists and albums.
