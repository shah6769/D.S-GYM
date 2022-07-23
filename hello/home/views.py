from unicodedata import name
from django.shortcuts import render,HttpResponse
from home.models import contact
from django.contrib import messages


# Create your views here.
def index(request):
    return render( request,'index.html')

def about(request):
    return render( request,'about.html')

def services(request):
     return render( request,'services.html')

def contact(request):
     if request.method =="post":
          name= request.POST.get('name')
          email =request.POST.get('email')
          message=request.POST.get('message')
          contact = contact(name=name,email=email,message=message)
          contact.save()
          messages.success(request, 'Profile details updated.')


     return render( request,'contact.html')

def login(request):
     return render( request,'login.html')