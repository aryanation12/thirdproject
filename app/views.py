from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
 return HttpResponse('I hate you django')
