from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def about_project(request):
    return HttpResponse('This is the about page')
