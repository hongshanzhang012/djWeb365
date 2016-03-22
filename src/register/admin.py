from django.contrib import admin
from register.models import Register
from register.models import UrlContent
from register.models import test


class RegisterAdmin(admin.ModelAdmin):
    list_display=('url','email', 'content_change', 'server_is_down')    
    
class UrlContentAdmin(admin.ModelAdmin):
    list_display=('url','md5','modified')    
    
# Register your models here.
admin.site.register(Register, RegisterAdmin)
admin.site.register(UrlContent, UrlContentAdmin)
admin.site.register(test)
