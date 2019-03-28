from django.shortcuts import render
from django.http import HttpResponse
def welcome(request):
    return HttpResponse("""<html><body bgcolor=pink><h1><center>Welcome To LokeshIT</center></h1></body></html>""")

# Create your views here.
