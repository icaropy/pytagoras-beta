# -*- coding: utf-8 -*-
from math import sqrt
def pitagoras(oposto=None,adjacente=None,hipotenusa=None):
	if oposto is None:
		oposto = float(sqrt(float(adjacente)**2 + float(hipotenusa)**2))
		return oposto
	if adjacente is None:
		adjacente = float(sqrt(float(oposto)**2 + float(hipotenusa)**2))
		return adjacente
	if hipotenusa is None:
		hipotenusa = float(sqrt(float(oposto)**2 + float(adjacente)**2))
		return hipotenusa
print "Pytagoras"
print "Insira os valores no formato:"
print "cateto oposto, cateto adjacente, hipotenusa."
print " ex: 2,3,0 = 2² + 3², retorna a hipotenusa."
print "ex2: 0,1,2 = 1² + 2², retorna o cateto oposto."
variaveis = []
linha = raw_input("~> :")
variaveis.append(linha.split(','))
try:
	variaveis = [map(float, x) for x in variaveis]
except: 
	pass
if len(variaveis[0][2]) == 0:
	print pitagoras(oposto=variaveis[0][0],adjacente=variaveis[0][1],hipotenusa=None)
elif len(variaveis[0][1]) == 0:
	print pitagoras(oposto=variaveis[0][0],adjacente=None,hipotenusa=variaveis[0][2])
else:
	print pitagoras(oposto=None,adjacente=variaveis[0][1],hipotenusa=variaveis[0][2])
