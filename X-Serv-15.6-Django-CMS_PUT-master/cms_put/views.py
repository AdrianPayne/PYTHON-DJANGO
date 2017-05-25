from django.shortcuts import render
from django.http import HttpResponse
from cms.models import Pages
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def insert(request):
    reply = """
        <form action="" method="post">
          Escribe tu nombre:
          <input type="text" name="name" value="" />
          <br/>
          <br/>
          Escribe la página:
          <input type="text" name="page" value="" />
         
          <br/>
         
          <input type="submit" value="Enviar" />
        </form>
        """
    if request.method == "PUT" or request.method == "POST":
        body = str(request.body)
        name = body.split('&')[0].split('=')[1]
        page = body.split('&')[1].split('=')[1][:-1]
        guardar = Pages(name=name, page=page)
        guardar.save()

    return HttpResponse(reply)
