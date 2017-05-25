#!/usr/bin/python3

"""
webApp class
 Root for hierarchy of classes implementing web applications

 Copyright Jesus M. Gonzalez-Barahona and Gregorio Robles (2009-2015)
 jgb @ gsyc.es
 TSAI, SAT and SARO subjects (Universidad Rey Juan Carlos)
 October 2009 - February 2015
"""

import socket
import urllib.parse

#funcion: rellena diccionarios con el archivo
def inic_texto(urls, numeros):
    lineas_url = fich.readlines()
    t = 0
    for i in lineas_url:
        url = lineas_url[t].split()[0]
        value = lineas_url[t].split()[1]

        urls[url] = value
        numeros[value] = url

        t = t + 1

#funcion: actualiza los diccionarios con cada POST
def put_texto(url, indice):
    fich.write(url + " " + indice + "\n")

def dame_lista():
    lista = ("LISTA DE URL's acortadas<br>")
    for enlace in dici1:
        lista =  (lista + enlace + " | http://localhost:1234/" + dici1[enlace] + "<br>")
    return lista

class webApp:

    def parse(self, request):
        interaccion = str(request.split()[0])[2:-1]
        if interaccion == "GET":
            print ("PARSE: Recibido un get\n")
            # Puede venir vacio o con recurso
            recurso = str(request.split()[1])[3:-1]
            if len(recurso) != 0:
                # Recurso -> Redireccion HTTP
                interaccion = interaccion + " " + recurso
            else:
                # Recurso vacio -> Solo formulario
                interaccion = (interaccion + " formulario246808642")

        elif interaccion == "POST":
            print ("PARSE: Recibido un post\n")
            urlnativ = str(request.split()[-1])[6:-1]
            urlnativ = str(urllib.parse.unquote(urlnativ, 'utf-8', 'replace'))
            # Comprobamos si lleva prefijo http, si no se lo ponemos
            if not (urlnativ[0:7] == "http://" or urlnativ[0:8] == "https://"):
                url = "http://" + urlnativ
            else:
                url= urlnativ
            print("urlnativ: " + urlnativ + "|\n" + "url: " + url + "|")

            # Post vacio o con recurso (este a su vez ya usado o no)
            print("Longitud de la URLnativa: " + str(len(urlnativ)))
            if len(urlnativ) != 0:
                # Comprobar si la entrada es nueva
                if not (url in dici1):
                    indice = 0
                    for enlaces in dici1:
                        indice = indice + 1

                    indice = str(indice)
                    dici1[url] = indice
                    dici2[indice] = url

                    put_texto(url, indice)

                interaccion = interaccion + " " + url
            else:
                #POST VACIO -> HTML ERROR
                interaccion = interaccion + " peticionvacia135797531"

        print("SALIDA PARSE: " + interaccion)
        return interaccion

    def process(self, parsedRequest):
        if parsedRequest.split()[0] == "POST":
            # Descarta al posibilidad de que el POST este vacio
            if parsedRequest.split()[1] != "peticionvacia135797531":
                numero = str(dici1[parsedRequest.split()[1]])
                respuesta = ("Url sin acortar: " + '<a href="' + parsedRequest.split()[1] + '">' + parsedRequest.split()[1] + '</a><br/>'
                + "Url acortada: " + '<a href=' + parsedRequest.split()[1] + '>' + "http://localhost:1234/" + numero 
                + "</a>")
            else:
                respuesta = "<h1>HTML ERROR: No se envio nada en el formulario</h1>"
            respuesta = ("200 OK", "<html><head><title> Acortador de URL's</title></head><body>" + respuesta + "</body></html>")
        else:
            # Descarta al posibilidad de que el GET este vacio 
            if parsedRequest.split()[1] != "formulario246808642":
                try:
                    url_redirec = dici2[parsedRequest.split()[1]]
                    respuesta = ("301 moved temporarily",
                    '<html><head><title> Acortador de URLs</title><meta http-equiv="Refresh" content=0;url=' + url_redirec
                    + '></head><body></body></html>')
                except KeyError:
                    respuesta = ("404 not found",
                    "<html><head><title> Acortador de URL's</title></head><body><h1>404 NOT FOUND</h1></body></html>")
            else:
                respuesta = ("<h3>Acortador de URL's</h3>"
                    + '<form action="http://localhost:1234" method="post">'
                    + 'Escribe una URL: <input type="text" name="url" value=""/>'
                    + "<br/>" 
                    + '<input type="submit" value="Enviar"/>'
                    + "</form>")
                lista = dame_lista()
                respuesta = ("200 OK", "<html><head><title> Acortador de URL's</title></head><body>" + respuesta + lista + "</body></html>")
        return respuesta

    def __init__(self, hostname, port):
        """Initialize the web application."""

        # Create a TCP objet socket and bind it to a port
        mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        mySocket.bind((hostname, port))

        # Queue a maximum of 5 TCP connection requests
        mySocket.listen(5)

        # Accept connections, read incoming data, and call
        # parse and process methods (in a loop)

        while True:
            print('Waiting for connections')
            (recvSocket, address) = mySocket.accept()
            print('HTTP request received (going to parse and process):')
            request = recvSocket.recv(2048)
            print(request.decode('utf-8'))
            parsedRequest = self.parse(request)
            (returnCode, htmlAnswer) = self.process(parsedRequest)
            print('Answering back...')
            recvSocket.send(bytes("HTTP/1.1 " + returnCode + " \r\n\r\n"
                            + htmlAnswer + "\r\n", 'utf-8'))
            recvSocket.close()

# COMIENZA LA EJECUCION

dici1 = {}
dici2 = {}
fich = open("lista_url.scv","r+")
inic_texto(dici1, dici2)

if __name__ == "__main__":
    testWebApp = webApp("localhost", 1234)
