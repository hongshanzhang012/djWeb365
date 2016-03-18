#link views with urls
#it is recommended that each app has a urls.py
# remember to add this urls.py tuple to project's urls.py

from django.conf.urls import patterns, url 
from register import views

#r'^$': regular express, represents an empty string
#tuple: like a list, an object

#(?P stands for the parameter that will be passed to the view)
#name='index', means name of the url
urlpatterns = [
               url(r'^$', views.register_page,name='register_page'),
               url(r'^register/', views.register_page,name='register_page'),
]

