from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact, Signin, Mador

# Create your views here.
def index(request):
      return render(request, 'index.html')

def matsa(request):
      return render(request, 'about.html')

def hofesh(request):
      if request.method=="POST":
            contact = Mador()
            name = request.POST.get('name')
            email = request.POST.get('email')
            file = request.POST.get('file')
            message = request.POST.get('message')
            contact.name = name
            contact.email = email
            contact.file = file
            contact.message = message
            contact.save()
            return HttpResponse('<h1>נרשמת בהצלחה</h1>')
      return render(request, 'hofesh-habitoi.html')

def mador(request):
      return render(request, 'hofesh-habitoi-img.html')

def signin(request):
      if request.method=="POST":
            contact = Signin()
            name = request.POST.get('name')
            email = request.POST.get('email')
            subject = request.POST.get('subject')
            number = request.POST.get('number')
            home = request.POST.get('home')
            date = request.POST.get('date')
            contact.name = name
            contact.email = email
            contact.subject = subject
            contact.number = number
            contact.home = home
            contact.date = date
            contact.save()
            return HttpResponse('<h1>נרשמת בהצלחה</h1>')
      return render(request, 'hiztarfut.html')

def kesher(request):
      if request.method=="POST":
            contact = Contact()
            name = request.POST.get('name')
            email = request.POST.get('email')
            subject = request.POST.get('subject')
            contact.name = name
            contact.email = email
            contact.subject = subject
            contact.save()
            return HttpResponse('<h1>נשלח בהצלחה</h1>')
            
      return render(request, 'contactus.html')