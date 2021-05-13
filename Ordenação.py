# -*- coding: utf-8 -*-

def Ordenacao_Palavras () :
	
	Lista = input(" Ordenar palavras -> ")
	Lista = Lista.split()
	Lista.sort()

	for i in Lista:
		print(i)

	escolha = input("Quer Ordenar novamente sim ou nao -> ")

	while escolha == "sim" :
		return Ordenacao_Palavras()

	if escolha == "nao" :
		return (0)
		
Ordenacao_Palavras()
