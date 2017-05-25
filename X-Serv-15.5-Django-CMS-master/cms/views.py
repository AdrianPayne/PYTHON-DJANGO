from django.shortcuts import render
from django.http import HttpResponse
from cms.models import Pages

# Create your views here.

def imprimir_todo(request):
    Lista = Pages.objects.all()
    reply = "<ol>"
    for contenido in Lista:
        reply += "<li><p>" + contenido.name + ": " + contenido.page
    reply += "</ol>"
    return HttpResponse(reply)
