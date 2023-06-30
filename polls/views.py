from django.shortcuts import render,redirect
from .models import Person
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required 
# Create your views here.
@login_required(login_url='/')
def homePage(request):
    return render(request, "index.html")
@login_required(login_url='/')
def first(request):
    return render(request, "first.html")
@login_required(login_url='/')
def all_data(request):
    data=Person.objects.all()
    return render(request, "data.html",{'data':data})

def login_page(request):

        if request.method =='POST':

            username = request.POST.get('username')
            password = request.POST.get('password')

            # if not User.objects.filter(username=username).exists():
            #      messages.error(request,'Invalid username')
            #      return redirect('/register/')
            
            user=authenticate(request,username=username,password=password)

            if user is None:
                 messages.error(request,'Invalid credentials')
                 return redirect('/register/')
            else:
                 login(request,user)
                 messages.success(request,'Successful')
                 return redirect('/first/')
        else:
             return render(request,'login.html')

def logout_page(request):
     logout(request)
     return redirect('/login/')


def register(request):

    if request.method =='POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user=User.objects.filter(username=username)
        
        if user.exists():
            messages.error(request,'Username already exists')
            return redirect('/register/')

        user=User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username,
            password=password
        )

        user.set_password(password)
        user.save()

        return redirect('/register/')

    return render(request,"register.html")