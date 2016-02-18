#!/usr/bin/python

# Algoritmo YYC
# Desarrollador por: Guerrero Arreola Alejandra
# Descripcion: Implementación en Python del algoritmo YYC

# -------------------------------------------------------------------------------------
# ---------------------------- Libraries ----------------------------------------------
# -------------------------------------------------------------------------------------

import os
import collections
import argparse
import json

# -------------------------------------------------------------------------------------
# ---------------------------- Functions ----------------------------------------------
# -------------------------------------------------------------------------------------

# Funcion que imprime la matriz
def print_matrix(matrix):
	for line in matrix:
		print ("\t",line)

# Funcion que verifica si hay unos en los renglones
def intersection_lists(actual_row, ones):
	intersection = [x for x in actual_row if x in ones]
	return intersection

# Funcion que concatena dos listas
def append_lists(list1, list2):
	aux = []
	aux.extend(list1)
	aux.extend([list2])
	aux.sort()
	return aux

# Funcion que genera la sub matriz
def create_sub_matrix(matrix, columns, rows):
	sub_matrix = []
	for line in range(0,rows+1):
		aux = []
		for x in columns:
			aux.append(matrix[line][x])
		sub_matrix.append(aux)
	return sub_matrix

# Funcion que determina si un conjunto es compatible
def compatible_set(matrix, columns, rows):
	min_matrix = create_sub_matrix(matrix, columns, rows)
	ones_list = {}
	flag = True
	
	for x in range(len(min_matrix)):
		elements_in_line = collections.Counter(min_matrix[x])
		if elements_in_line[1] == 1:
			pos_one = min_matrix[x].index(1)
			if ones_list.get(pos_one, False):
				ones_list[pos_one].append(x)
			else:
				ones_list[pos_one] = [x]

	for x in range(len(min_matrix[0])):
		if not ones_list.get(x, False):
			flag = False
			break

	return flag

# -------------------------------------------------------------------------------------
# ---------------------------- YYC algotithm ------------------------------------------
# -------------------------------------------------------------------------------------

def yyc_algorithm(matrix,print_steps=False):
	hits = 0

	# imprime matriz de entrada
	print("Matriz de entrada:")
	print_matrix(matrix)

	# Ingresar los unos del primer renglon a la pila Ψ
	Ψ = [[x] for x,y in enumerate(matrix[0]) if y == 1]
	max_len = len(Ψ)
	
	# Recorrer cada fila de la matriz
	for i in range(1, len(matrix)):
		Ψaux = []

		for element in Ψ:
			ones = [x for x,y in enumerate(matrix[i]) if y == 1]
			if (len(intersection_lists(element, ones)) != 0):
				hits += 1
				Ψaux.append(element)

			else:
				for x in ones:
					hits += 1
					sub_matrix = append_lists(element,x)
					if(compatible_set(matrix, sub_matrix, i)):
						Ψaux.append(sub_matrix)
		
		if (print_steps):
			print('Ψaux', i, ':')
			print_matrix(Ψaux)

		# Actualizar la pila Ψ
		Ψ = Ψaux

		# Tamaño maximo de la lista
		if (max_len < len(Ψ)):
			max_len = len(Ψ)

	# Imprir testores tipicos
	print('\n\n=== Testores típicos === \n')
	for testor in Ψ:
		print(testor)

	print('\nLongitud Ψ:', len(Ψ))
	print('Hits:', hits)
	print('max_len:', max_len)
	return


# -------------------------------------------------------------------------------------
# ---------------------------- Main Code ----------------------------------------------
# -------------------------------------------------------------------------------------

if __name__ == '__main__':

	# Limpiar consola
	os.system('clear')

	print("Algoritmo YYC\n")

	# Matrices
	matrix = {

		"articulo_br" :	[
			[1,0,0,0,0,0,0,1,0],
			[0,1,0,0,0,1,0,0,0],
			[0,0,0,1,1,1,1,0,1],
			[0,0,1,0,1,0,0,1,1],
			[1,0,0,0,1,0,0,0,1]
		],
		"n2" : 	[
			[1,1,1,0,0],
			[1,1,0,0,1],
			[1,0,1,1,0],
			[1,0,1,0,1]
		],
		"s" : 	[
			[1,0,0,0,1,0],
			[1,1,0,0,0,1],
			[0,0,1,0,0,1],
			[1,0,0,1,0,1]
		],
		"identidad_basica" : [
			[0,0,0,1],
			[1,0,0,0],
			[0,0,1,0],
			[0,1,0,0]
		]
	}

	# Establecer opcines de entrada
	parser = argparse.ArgumentParser( description = 'Implementación en Python del algoritmo YYC.' )
	parser.add_argument('-m', '--matriz',
						nargs = '?',
						action = 'store',
						dest = 'matrix',
						choices=['articulo_br','identidad_basica','n2', 's'],
						default = 'articulo_br',
						help = 'Selecciona la matriz a analizar: articulo_br,identidad_basica,n2,s' )

	parser.add_argument('-f', '--file',
						nargs = '?',
						dest = 'matrix_file',
						default = False,
						help = 'Inserta una matriz desde un archivo json' )

	parser.add_argument('-i', '--imprimir_pasos',
						nargs = '?',
						action = 'store',
						dest = 'print_steps',
						choices = ['Y', 'N'],
						default = 'N',
						help = 'Muestra los pasos del algoritmo YYC: Y(si), N(No)' )

	options = parser.parse_args()


	if (options.matrix_file):
		with open(options.matrix_file,'r') as json_file:
			matrix_file = json.load(json_file)
		matriz_seleccionada = matrix_file["matrix"]
	else:
		matriz_seleccionada = matrix[options.matrix]

	if (options.print_steps == 'Y'):
		yyc_algorithm(matriz_seleccionada, True)
	else :
		yyc_algorithm(matriz_seleccionada, False)