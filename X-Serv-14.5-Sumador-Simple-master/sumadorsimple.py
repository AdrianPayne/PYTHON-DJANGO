#!/usr/bin/python3

"""
Simple HTTP Server
Jesus M. Gonzalez-Barahona and Gregorio Robles
{jgb, grex} @ gsyc.es
TSAI, SAT and SARO subjects (Universidad Rey Juan Carlos)
"""

import socket

# Create a TCP objet socket and bind it to a port
# We bind to 'localhost', therefore only accepts connections from the
# same machine
# Port should be 80, but since it needs root privileges,
# let's use one above 1024

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
mySocket.bind((socket.gethostname(), 1234))

# Queue a maximum of 5 TCP connection requests

mySocket.listen(5)

# Accept connections, read incoming data, and answer back an HTML page
#  (in an infinite loop)

num = 0
flag = True

while True:
    entrada_correcta = True
    print('Waiting for connections')
    (recvSocket, address) = mySocket.accept()
    recibido = str(recvSocket.recv(1024).decode('utf-8'))
    num = (recibido.split()[1][1:])
    print('HTTP request received:' + recibido)

    if num == 'favicon.ico':
        print ("NAVEGADOR PIDE FAVICON: ")
        entrada_correcta = False
    else:
        num = int(num) ## Asumo que al entrada siempre seran numeros enteros (ni strings ni floats)
        if flag and entrada_correcta:
            print(num)
            recvSocket.send(bytes("HTTP/1.1 200 OK\r\n\r\n" +
                            "<html><body><h1>" +
                            "Me has enviado un " + str(num) + ". Dame más."
                            "</h1></body></html>" +
                            "\r\n", 'utf-8'))
            num_2 = num
            flag = False
        elif not flag and entrada_correcta:
            print(num)
            recvSocket.send(bytes("HTTP/1.1 200 OK\r\n\r\n" +
                            "<html><body><h1>" +
                            "Me has enviado un " + str(num_2) + ". Ahora un " + str(num) + ". La suma es " + str((num + num_2)) +
	                        "</h1></body></html>" +
                            "\r\n", 'utf-8'))
            flag = True
    print(num)
