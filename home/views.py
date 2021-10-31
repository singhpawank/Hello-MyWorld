from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from home.models import Contact

from django.contrib import messages
from datetime import datetime

# Create your views here.

def index(request):
    context = {
        "variable" : "sent"
    }
    return render(request, 'index.html', context)
    #return HttpResponse("This is homepage")

def about(request):
    return render(request, 'about.html')

def blog(request):
    return render(request, 'blog.html')

def contact(request):
    if(request.method=='POST'):
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')      
        #if len(name)<2 or len(email)<4 or len(phone)<10 or len(content)<5:
            #messages.error(request, 'Sorry ,please fill the form in a right manner')
        #else:
        contact=Contact(name=name,email=email,phone=phone,desc=desc)
        contact.save()
        messages.success(request, 'Form submitted successfully!')
        
    return render(request, 'contact.html')



