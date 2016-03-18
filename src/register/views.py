from django.shortcuts import render
from register.models import Register
from register.forms import RegisterForm
from django.contrib import messages

# Create your views here.
#each view exists as a function, 

#inside your app folder, create urls.py to map this view and url

def register_page(request):
    # A HTTP POST?
    if request.method == 'POST':
        form = RegisterForm('titleA-reserved','descriptionA-reserved',request.POST) 
        # Have we been provided with a valid form?
        if form.is_valid():
            # Not all fields are automatically populated!
            page = form.save(commit=False)
            # With this, we can then save our new model instance.
            page.save()
            messages.success(request, 'url successfully added to watch list.')
            # The user will be shown the homepage.
            #return register_page(request)
            form = RegisterForm('saved','descriptionA-reserved')

        else:
            # The supplied form contained errors - just print them to the terminal.
            print (form.errors)
    else:
        # If the request was not a POST, display the form to enter details.
        form = RegisterForm('new','descriptionA-reserved')
    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    #path  'rango/add_page.html' is the template directory, not the url address path
    return render(request, 'register/register.html', {'form': form})
