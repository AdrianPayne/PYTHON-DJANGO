from django.shortcuts import render
from django.http import HttpResponse
from acorta.models import Pages
from django.views.decorators.csrf import csrf_exempt
import urllib.parse

# Create your views here.

@csrf_exempt

def main(request):
    reply = """
        <form action="" method="post">
          Escribe una URL:
          <input type="text" name="url" value="" />
          <br/>

          <input type="submit" value="Enviar" />
        </form>

        """
    Lista = Pages.objects.all()
#CUANDO: Usuario introduce una pagina web
    if request.method == "PUT" or request.method == "POST":
        body = str(request.body)
        url = body.split('&')[0].split('=')[1][:-1]
        url = str(urllib.parse.unquote(url, 'utf-8', 'replace'))

        if not (url.startswith("http://") or url.startswith("https://")):
            url = "http://" + url

# Comprueba que no esta en la lista antes de guardarlo
        ready = False
        for contenido in Lista:
            if url in contenido.url:
                ready = True
        if not ready:
            guardar = Pages(url=url, page=len(Lista))
            guardar.save()

    Lista = Pages.objects.all()

#Volcamos la base de datos en Lista y la imprimimos
    reply += "<br/>------------------------------------------------------------"

    reply += "<h1>LISTA</h1>"
    reply += "<ul>"

    for contenido in Lista:
        reply += "<li><p>" + '<a href="' + contenido.url + '">' + contenido.url + "<a/>: " + str(contenido.page)
    reply += "</ul>"

    return HttpResponse(reply)

def recurso(request, num):
#Encontrar la url a partir del numero
    Lista = Pages.objects.all()
    try:
        url = Lista[int(num)].url
        reply = ('<head><meta http-equiv="Refresh" content="0;url=' + url + '"></head>')
    except:
        reply = '<head><meta http-equiv="Refresh" content="3;url=http://localhost:8000"></head><h1>Ese recurso no existe primo</h1>'
    return HttpResponse(reply)

def error(request):

    return HttpResponse('<head><meta http-equiv="Refresh" content="3;url=http://localhost:8000"></head><h1>RECURSO INVALIDO</h1> Tiene que ser un numero')
