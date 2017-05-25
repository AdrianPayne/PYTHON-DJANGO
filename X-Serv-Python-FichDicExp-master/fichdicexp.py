#!/usr/bin/python3
fich = open("/etc/passwd", "r")
identificadores = fich.readlines()
fich.close()
usuarios = {}

for itiner in range(0, len(identificadores)):
	i = 0
	n = -1
	while identificadores[itiner][i] != ":":
		i = i + 1
	while identificadores[itiner][n] != ":":
		n = n - 1
	usuarios[identificadores[itiner][0:i]] = identificadores[itiner][n+1:-1]

print("root: " + usuarios['root'])
try:
	print("imaginario: " + usuarios['imaginario'])
except KeyError:
	print("No existe imaginario")

