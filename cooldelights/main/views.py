from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from main.models import Contact
# Create your views here.
def home(request):
    return render(request,"home.html")
def about(request):
    return render(request,"about.html")
def contact(request):
    if request.method=="POST":
        e=request.POST.get('email')
        n=request.POST.get('name')
        p=request.POST.get('phone')
        d=request.POST.get('desc')
        print(n)
        print(e)
        print(p)
        print(d)
        con=Contact(email=e,name=n,phone=p,desc=d)
        con.save()
        

    return render(request,"contact.html")
