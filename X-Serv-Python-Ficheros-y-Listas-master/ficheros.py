#!/usr/bin/python3
fich = open("/etc/passwd", "r")
identificadores = fich.readlines()
for itiner in range(0, len(identificadores)):
	i = 0
	n = -1
	while identificadores[itiner][i] != ":":
		i = i + 1
	while identificadores[itiner][n] != ":":
		n = n - 1
	print("User: " + identificadores[itiner][0:i] + " | Shell: " + identificadores[itiner][n+1:-1])
print("\n" + "Usuarios en la maquina: " + str(len(identificadores)))
