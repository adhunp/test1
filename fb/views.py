from django.shortcuts import render

# Create your views here.

def fb(request):
    return render (request,'fb.html')

def signup(request):
    return render (request,'signup.html')

def home(request):
    return render (request,'home.html')