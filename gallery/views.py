from django.shortcuts import render
from django.http import HttpResponse

def index(reques):
    text_var = 'Ferguson Art Gallery Shop'
    return HttpResponse(text_var)    