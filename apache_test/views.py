from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>Congratulations, Django works.</h1>')