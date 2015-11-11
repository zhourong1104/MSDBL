from django.shortcuts import render
from django.http.response import HttpResponse
# Create your views here.


def home(request):
    f = open('Templates/homepage.html','r')
    return HttpResponse(f.read())

def work(request):
    f = open('Templates/work.html','r')
    return HttpResponse(f.read())

def tool(request):
    f = open('Templates/tool.html','r')
    return HttpResponse(f.read())

def ftp(request):
    f = open('Templates/ftp.html','r')
    return HttpResponse(f.read())