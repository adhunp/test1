from django.shortcuts import render

# Create your views here.

def adhun(request):
    return render (request,'adhun.html')

def athul(request):
    return render (request,'athul.html')