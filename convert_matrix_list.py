#!/usr/bin/python

# Algoritmo YYC
# Desarrollador por: Silva Peña Guillermo
# Descripcion: Convertir matrix en lista de incidencia

# -------------------------------------------------------------------------------------
# ---------------------------- Libraries ----------------------------------------------
# -------------------------------------------------------------------------------------

import os
from main import print_matrix
import argparse
import json

# -------------------------------------------------------------------------------------
# ---------------------------- Functions ----------------------------------------------
# -------------------------------------------------------------------------------------
def convert_matrix_to_list(matrix,filename):
	# imprime matriz de entrada
    #print("Matriz de entrada:")
    #print_matrix(matrix)
    new_matrix = []
    for list in matrix:
        new_list = []
        for x in range(len(list)):
            if(list[x]==1):
                new_list.append(x)
        new_matrix.append(new_list)
    #print_matrix(new_matrix)
    with open("incidence_list_"+filename, 'w') as f:
        json.dump({"matrix":new_matrix}, f, ensure_ascii=False)

def convert_list_to_matrix(matrix,filename):
	# imprime matriz de entrada
    #print("Matriz de entrada:")
    #print_matrix(matrix)
    new_matrix = []
    max_v = -1
    for list in matrix:
        if(max(list)>max_v):
            max_v = max(list)

    for list in matrix:
        new_list = []
        for x in range(max_v+1):
            if(x in list):
                new_list.append(1)
            else:
                new_list.append(0)
        new_matrix.append(new_list)
    #print_matrix(new_matrix)
    with open("matrix_"+filename, 'w') as f:
        json.dump({"matrix":new_matrix}, f, ensure_ascii=False)

# -------------------------------------------------------------------------------------
# ---------------------------- Main Code ----------------------------------------------
# -------------------------------------------------------------------------------------

if __name__ == '__main__':

    parser = argparse.ArgumentParser( description = 'Convertir matrix a lista de incidencia.' )
    parser.add_argument('-m', '--matriz',
    nargs = '?',
    dest = 'matrix_file',
    default = False,
    help = 'Inserta una matriz desde un archivo json y convertirla a lista de incidencia.' )

    parser.add_argument('-l', '--list',
    nargs = '?',
    dest = 'list_file',
    default = False,
    help = 'Inserta una lista de incidencia desde un archivo json y convertirla a una matriz.' )

    options = parser.parse_args()

    if (options.matrix_file):
        with open(options.matrix_file,'r') as json_file:
            matrix_file = json.load(json_file)
        convert_matrix_to_list(matrix_file["matrix"],options.matrix_file)

    if (options.list_file):
        with open(options.list_file,'r') as json_file:
            list_file = json.load(json_file)
        convert_list_to_matrix(list_file["matrix"],options.list_file)

    print("Listo!!!!")
