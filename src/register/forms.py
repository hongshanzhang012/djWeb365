from django import forms
from register.models import Register

class RegisterForm(forms.ModelForm):
    url = forms.URLField(widget=forms.TextInput(attrs={'class' : 'text_box'}), max_length=128, label="url you want to register:")
    email = forms.EmailField(widget=forms.TextInput(attrs={'class' : 'text_box'}), max_length=128, label="Send email to:")

    #required=False indicate form validation will not require it.
    content_change = forms.BooleanField(widget = forms.CheckboxInput(attrs={'class' : 'check_box'}), label="Content change", initial=False, required=False)
    server_is_down = forms.BooleanField(widget = forms.CheckboxInput(attrs={'class' : 'check_box'}), label="Server is down", initial=False, required=False)
        
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Register
        # What fields do we want to include in our form?
        # This way we don't need every field in the model present.
        # Some fields may allow NULL values, so we may not want to include them...
        # Here, we are hiding the foreign key.
        fields = ('url', 'email', 'content_change', 'server_is_down')

    #override method clean to accept url that does not start with 'http://'
    # it seems override clean() methods is not working???? 
    def clean(self):
        cleaned_data = self.cleaned_data
    
        url = cleaned_data.get('url')
        # If url is not empty and doesn't start with 'http://', prepend 'http://'.
        if url and not url.startswith('http://'):
            url = 'http://' + url
            cleaned_data['url'] = url
        return cleaned_data
  
    def __init__ (self, title, desc, *args, **kwargs):
        self.title = title
        self.desc = desc
        super (RegisterForm, self).__init__ (*args, **kwargs) # call base class
        