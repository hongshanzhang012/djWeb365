"""
WSGI config for djWeb365 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djWeb365.settings")

application = get_wsgi_application()

"""
django servers:
1) django development server
django-admin.py runserver

2) apache + mod_wsgi

3) uwsgi+ nginx
          apache
          cherokee
          etc
          
4) gunicorn (webserver for python app)
like unicorn for ruby

wsgi: web service gateway interface for python app

our solution is: 3) +4) gunicorn + nginx
nginx +uwsgi: webserver (http serfver) serve static content
gunicorn: app server, serve dynamic content

#using the following command to start gunicorn
#navigate to project folder where manage.py resides.
gunicorn djWeb365.wsgi #use virtual env
#to stop service: ctrl+c

#call gunicorn in background
gunicorn djWeb365.wsgi &
to stop service: use process manager

reload app:
ps -xa | grep gunicorn
kill -HUP 23435

"""

"""
config nginx
#if you have virtual env, copy static folder to env, do not put it in your app folder

under folder in /etc/nginx/sites-available/, create file djWeb365:
server {
    server_name 10.1.1.82;
    listen       8080; #80 is occupied by ipsw already
    server_name  url365.com www.url365.com;
    root         /var/www/djWeb365/;
    
    access_log off;

    location /static/ {
        alias /var/www/djWeb365/env/static/;
    }

    location / {
        proxy_pass http://10.1.1.82:8000;
        proxy_set_header X-Forwarded-Host $server_name;
        proxy_set_header X-Real-IP $remote_addr;
        add_header P3P 'CP="ALL DSP COR PSAa PSDa OUR NOR ONL UNI COM NAV"';
    }
}

cd /etc/nginx/sites-enabled
sudo ln -s ../sites-available/djWeb365
sudo rm default
sudo service nginx restart

now navigate to project folder and start gunicorn:
cd /var/www/djWeb365/src

"""

"""
virtualenv and permission 

web applications should run as system users with limited privileges
in my case, I use sgroup 'webapps' and user 'djWeb365'
$ sudo groupadd --system webapps
$ sudo useradd --system --gid webapps --shell /bin/bash --home /var/www/djWeb365 djWeb365
#owner djWeb365 and group owner 'nick' has full access to folder djWeb365
sudo chown -R djWeb365:nick /var/www/djWeb365/
sudo chmod -R 775 /var/www/djWeb365

#install virtualenv on specified python version, mine is python 2.7.11
#****************install env*************************#
virtualenv -p /usr/local/lib/python2.7.11/bin/python env

sudo su - djWeb365
source env/bin/activate #use deactivate to exit virtualenv
activate the virtualenv and then: 
pip install django
pip install psycopg2 #django interface to postgre db 
pip install gunicorn

#****************or clone env*************************#
git clone https://github.com/hongshanzhang012/djWeb365.git djWeb365

then inside src directory run gunicorn djWeb365.wsgi, ctrl+c to exit #use virtual env

gunicorn djWeb365.wsgi:application --env DJANGO_SETTINGS_MODULE='djWeb365.settings.development'

"""

"""
virtualenv on eclipse
create new interpreter: Window->Preferences... > PyDev > Interpreters > Python Interpreter
set your project to use this new interpreter
If you later install additional libraries, you will need to go back to the interpreter definitions,
 click "Apply", and tell Pydev which interpreters it should scan again. Until you do that, 
 PyDev might not notice your new libraries

"""

"""
git
https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging
#install git
sudo apt-get install git

git init #create git folder under project folder
git status -s (long or short) 
git add . #add project tree index. call it everytime the project tree changed
git commit -m "commit messate" # m stands for commit message
git commit -a # omit git add .
git reset HEAD -- hello.py #unstage the file
git reset --soft HEAD~ #undo last commit and them back on stage
git reset --hard HEAD #discard all changes since last commit
git rm file #remove file from index
git stash file #save changes in somewhere, not commit the changes for now.

git checkout -b iss53 #Switched to a new branch "iss53"
git checkout master
git merge hotfix
git branch -d hotfix #Deleted branch hotfix (3a0874c).

#remote link named as "origin", usr/pass: gmail, g2
git remote add origin https://github.com/hongshanzhang012/djWeb365.git
#this branch will be our master branch
git push -u origin master

#clone a copy on deploy server
git clone origin djWeb365
git pull origin djWeb365

"""





