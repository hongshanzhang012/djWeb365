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

using the following command to start gunicorn
navigate to project folder where manage.py resides.
gunicorn djWeb365.wsgi

to stop service: ctrl+c

"""

"""
config nginx
#if you have virtual env, copy static folder to env, do not put it in your app folder

under folder in /etc/nginx/sites-available/, create file djWeb365:
server {
    server_name 127.0.0.1;

    access_log off;

    location /static/ {
        alias /var/www/djWeb365/env/static/;
    }

    location / {
        proxy_pass http://127.0.0.1:8000;
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
owner djWeb365 and group owner 'nick' has full access to folder djWeb365
sudo chown -R djWeb365:nick /var/www/djWeb365/
sudo chmod -R 775 /var/www/djWeb365

install virtualenv on specified python version, mine is python 2.7.11
virtualenv -p /usr/local/lib/python2.7.11/bin/python env

sudo su - djWeb365
source env/bin/activate #use deactivate to exit virtualenv
activate the virtualenv and then: 
pip install django
pip install psycopg2 #django interface to postgre db 
pip install gunicorn
then inside src directory run gunicorn djWeb365.wsgi, ctrl+c to exit

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







