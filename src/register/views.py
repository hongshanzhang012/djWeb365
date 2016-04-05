from django.shortcuts import render
from register.models import Register
from register.forms import RegisterForm, UrlListForm
from django.contrib import messages
import psycopg2
#note that we have to import the Psycopg2 extras library!
import psycopg2.extras
import email

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

def new_delete_page(email, request,urls=None):
    if not urls:
        conn_string = "host='127.0.0.1' dbname='urlcrawler' user='postgres_nick' password='postgres_nick'"
        conn = psycopg2.connect(conn_string)
        cur = conn.cursor()
        sql="SELECT url FROM register_register WHERE email='"+email + "'"
        cur.execute(sql)             
        rows = cur.fetchall()
        if not rows:#all urls have been deleted
            form = RegisterForm('new','descriptionA-reserved')
            cur.close()
            conn.close()
            return render(request, 'register/register.html', {'form': form})
        else:
            form = UrlListForm(email, rows)
        
            cur.close()
            conn.close()
        
            return render(request, 'register/delete.html', {'form': form})
    else:
            form = UrlListForm(email, rows)
            return render(request, 'register/delete.html', {'form': form})
        

def delete_page(request):
    
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        if request.POST.get('delete'):
            # create a form instance and populate it with data from the request:
            email=request.POST.get('email')
            urls=request.POST.getlist('urls')
            if(len(urls)<=0):
                return new_delete_page(email, request, None)
                            
            t=()
            for url in urls:
                t1=(url,)
                t=(t+(t1,))               

            form = UrlListForm(email,t, request.POST)
            # check whether it's valid 
            if form.is_valid():
                # process the data in form.cleaned_data as required
                email=form.cleaned_data['email']
                urls=form.cleaned_data['urls']
                #delete records
                for url in urls:
                    Register.objects.filter(email=email ,url=url).delete()
    
                # redirect to a new URL:
                return new_delete_page(email, request, None)
                        
        elif request.POST.get('save'):
            #save records, will not run in this case, keep it here for future reference
            # create a form instance and populate it with data from the request:
            form = UrlListForm(request.POST, email=None) 
            # check whether it's valid:
            if form.is_valid():
                # process the data in form.cleaned_data as required
                
    
                # With this, we can then save our new model instance.
                page = form.save(commit=False)
                page.save()
                
                messages.success(request, 'Operation successful.')
    
                # redirect to a new URL:
                form = UrlListForm(email, url)
    else:
        # if a GET (or any other method) we'll create a blank form
        email=request.GET.get('email')
        url=request.GET.get('url')
        
        #below code is to verify integrity of the http request, these code is not reliable.
        conn_string = "host='127.0.0.1' dbname='urlcrawler' user='postgres_nick' password='postgres_nick'"
        conn = psycopg2.connect(conn_string)
        cur = conn.cursor()
        sql="SELECT * FROM register_register WHERE email='"+email + "' AND url='"+ url+"'"
        cur.execute(sql)             
        rows = cur.fetchone()
        cur.close()
        conn.close()
        if not rows:#all urls have been deleted
            # redirect to a new URL:
            form = RegisterForm('new','descriptionA-reserved')
            return render(request, 'register/register.html', {'form': form})            
        else:
            return new_delete_page(email, request, None)

