from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def suma(request, num1, num2):
    reply = int(num1) + int(num2)
    return HttpResponse(reply)

def resta(request, num1, num2):
    reply = int(num1) - int(num2)
    return HttpResponse(reply)

def producto(request, num1, num2):
    reply = int(num1) * int(num2)
    return HttpResponse(reply)

def division(request, num1, num2):
    try:
        reply = float(num1) / float(num2)
    except:
        reply = "No se puede dividir entre 0"
    return HttpResponse(reply)
