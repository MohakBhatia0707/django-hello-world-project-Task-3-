from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# def index(request):
#     return render(request,'Hello World')

def home(request):
    return HttpResponse('Hello World')