from django import forms
from register.models import Register
from distutils.tests.test_archive_util import UID_GID_SUPPORT

class RegisterForm(forms.ModelForm):
    url = forms.URLField(widget=forms.TextInput(attrs={'class' : 'text_box'}), max_length=128, label="url you want to watch:")
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
        if url:
            if not url.startswith('https://') and not url.startswith('http://'):
                url = 'http://' + url
                cleaned_data['url'] = url
        return cleaned_data
  
    def __init__ (self, title, desc, *args, **kwargs):
        self.title = title
        self.desc = desc
        super (RegisterForm, self).__init__ (*args, **kwargs) # call base class
        
        
class UrlListForm(forms.Form):
    #use Form instead of ModelForm since I do not have a field 'urls', I only have 'url'
    
    '''
    *args: not sure how many arguments might be passed to your function
    **kwargs: Named arguments (dict)    
    '''
    
    def __init__(self,email=None, urls=None,*args, **kwargs):
        super(UrlListForm, self).__init__(*args, **kwargs)
        '''
        GENDER_CHOICES = (
            (1,'male'),
            (2,'female'),
        )
        # If you would like to add extra choices, then you can do the following:
        GenDER_CHOICES.insert(0, ["Empty"])
    
        genders = forms.MultipleChoiceField(choices=GENDER_CHOICES, 
                                            widget=forms.CheckboxSelectMultiple(),
                                            initial=[gender[0] for gender in GENDER_CHOICES])
        '''

        if email and urls:
            self.fields['email'] = forms.CharField(label='email', initial=email,widget = forms.HiddenInput(), required=False)
            #qs=Register.objects.filter(email=email)
            choices=() #(tuple,), [list]
            
            for url in urls:
                l=((url[0],url[0]))
                t=tuple(l)
                choices=(choices+(t,))               
            
            self.fields['urls'] = forms.MultipleChoiceField(choices=choices, widget=forms.CheckboxSelectMultiple())

                
    '''         
    def __init__(self, email, *args, **kwargs):
        super(UrlListForm, self).__init__(*args, **kwargs)

        queryset=Register.objects.filter(email=email)
        # Set choices from argument.
        self.fields['email'] = forms.CharField(label='email', initial=email,widget = forms.HiddenInput(), required=False)
        #self.fields['urls'].widget.choices = choices
        self.fields['urls'].queryset=queryset
            
        #else:
            #tuple=list, only tuple is readonly, dict=key+value
        choices=[]
        urls=args[0].getlist('urls')
        for url in urls:
            choices.append(('1',url))
        #email=args[0].get('email', None)
      
    
    
    
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Register
        # What fields do we want to include in our form?
        # This way we don't need every field in the model present.
        # Some fields may allow NULL values, so we may not want to include them...
        # Here, we are hiding the foreign key.
        fields = ('url', 'email')
    '''
        
        