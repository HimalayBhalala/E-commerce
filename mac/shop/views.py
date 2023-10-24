from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request,'shop/index.html')

def about(request):
    return render(request,'shop/about.html')

def contact(request):
    return HttpResponse("This is use for contact me!")

def tracker(request):
    return HttpResponse("This is used for track a product")

def search(request):
    return HttpResponse("This is a seach page.")

def prodView(request):
    return HttpResponse("This is used for View Product")

def checkout(request):
    return HttpResponse("This is used for chechout...")