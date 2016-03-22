from django.db import models
from dns.rdatatype import NULL

# Create your models here.
class Register(models.Model):
    url=models.CharField(max_length=128)
    email=models.CharField(max_length=128)    
    
    #blank=True allows the value is empty in forms
    content_change=models.BooleanField(default=False, blank=True)
    server_is_down=models.BooleanField(default=False, blank=True)
    
    def __unicode__(self):
        return self.email  
    
"""    
create these tables
in terminal, run python manage.py syncdb
or use migrate. this is better option. It does not require deleting the db file everytime

db superuser created as nick, nick, hongshanzhang012@gmail.com
open system shell and navigate to project folder, run python manage.py createsuperuser
"""

class UrlContent(models.Model):
    url=models.CharField(max_length=128, primary_key=True)
    md5=models.CharField(max_length=32, default='', blank=True)
    modified=models.DateTimeField(blank=True)    
    
    def __unicode__(self):
        return self.url  
    
    
class test(models.Model):
    url=models.CharField(max_length=128)
    md5=models.CharField(max_length=32, default='', blank=True)
    modified=models.DateTimeField(blank=True)    
    
    def __unicode__(self):
        return self.url  
    