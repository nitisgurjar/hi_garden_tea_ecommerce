from django.shortcuts import render,redirect
from . models import *
from django.contrib import messages

def about(request):
    return render(request,'about.html')

def contact(request):
    co=Person.objects.all()
    return render(request,'contact.html',{'co':co})

def home(request):
    pro=Product.objects.all()
    return render(request,'home.html',{'pro':pro})


def contacts(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        subject=request.POST['subject']
        message=request.POST['message']
        Person.objects.create(name=name,email=email,subject=subject,message=message)
        messages.success(request,' query submitted')
        return redirect('contact.html')

