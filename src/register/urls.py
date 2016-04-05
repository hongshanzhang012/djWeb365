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
               #use www.url365.com/delete/?email=nzhang@futuredial.com&url=www.baidu.com
               url(r'^delete/', views.delete_page,name='delete_page'),
#below is another way to pass parameters, this may go wrong since it uses regex.               
#               url(r'^delete/(?P<category_name_url>\w+)/add_page/$', views.delete_page, name='delete_page'), # NEW MAPPING!

]

'''
email=hongshanzhang012@gmail.com
url=http://www.baidu.com/

'''
