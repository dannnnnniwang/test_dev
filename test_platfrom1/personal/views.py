from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hello(request):

    name = request.GET.get("name","")

    if name == "":
        return HttpResponse("name is NoneType")

    return HttpResponse("Hello"  +  name)