from django.shortcuts import render, HttpResponse
from django.http import request

# Create your views here.


def index(request):
     # context = {
     #      "variable1": "ecommerce websites",
     #      "variable2": "this is for test",
          
     # }
     return render(request, 'index.html')
     # return HttpResponse("<h1> This is home page </h1>")


def about(request):
     return render(request, 'about.html')


def contact(request):
     return render(request, 'contact.html')


def services(request):
     return render(request, 'services.html')
