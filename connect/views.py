from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

#creating starting page 

def index(request):
    return HttpResponse('hello world')
