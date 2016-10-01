#!/usr/bin/python
# coding: UTF-8
#H**2 = C **2 + C **2
from math import sqrt


class teorema:
	def __init__(hip):
		print('Teorema de pitagoras *By:H4n0x*')
		x = [1,2]
		c = 3
		d = [0]
		while c != x:
			d = +1
			hip.de = int(input('Possui valor da hipotenusa ? , 2-Para NÂO:'))
			try:
				if hip.de == 2:
					hip.x = str(input('Informe valor da hipotenusa:'))
					hip.cat = int(input('Informe o cateto oposto:'))
					hip.cato = int(input('Informe o cateto adjacente: '))
					v_1 = hip.cat**2 + hip.cato**2
					print('X = %d' %(v_1))
					raiz = int(sqrt(v_1))
					print('Hipotenusa igual á %d' %(raiz))
			except:
				print('Hipotenusa x , Nos cateto somente números')
#chamando a classe
py = teorema()
#chamando metodo
py = hip()

			
