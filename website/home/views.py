from django.shortcuts import render , HttpResponse, redirect
from datetime import datetime
from home.models import Contact
from django.contrib import messages
from django.contrib.auth.models import auth 
from django.contrib.auth.models import User 

# Create your views here.
def index(request):
    if request.method == "POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        msg=request.POST.get('msg')
        contact=Contact(name=name, email=email,msg=msg ,date=datetime.today())
        contact.save()
       
    return render(request,"index.html")

def contact(request):
    if request.method == "POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        msg=request.POST.get('msg')
        contact=Contact(name=name, email=email,msg=msg ,date=datetime.today())
        contact.save()
        messages.success(request, 'your message is being send')

        #send email to user
        subject = 'Team Ghostpy <no-reply@shantanunimkar19@gmail.com>'
        message = 'Hi {name}, thank you for registering in geeksforgeeks.'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email]
        send_mail( subject, message, email_from, recipient_list )

    

    return render(request,"contact.html")

   
def dashboard(request):
    return render(request, "dashboard.html")


