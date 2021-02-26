#!/usr/bin/env python3
import math
def line_count():
    return sum(1 for line in  open("new_file.txt",'r'))


"""
    Abrindo o arquivo de texto
"""
file =  open("new_file.txt",'r')

"""
    Vetor que irá armazenar todos os valores do arquivo txt
"""
vetor = []

nLinhas = line_count()

colunas = 0
linhas = 0

"""
    For que armazena os valores do arquivo no vetor e calcula a quantidade de colunas presentes nas tabelas
"""
for line in file:
       linhas += 1
       for n in line.split(' '):
           if n != '\n' and n != 'setosa' and n!= 'virginica' and n !='versicolor' and n !='':
                colunas += 1
                vetor.append(float(n))
           elif n == 'setosa' or n== 'virginica' or n =='versicolor':
                colunas += 1
                vetor.append(n)

           if linhas != nLinhas :
                colunas= 0


"""
    Criação e preenchimento de uma matriz com os dados do arquivo txt
"""               
matrix = []
for i in range(linhas):
    matrix.append([0]*colunas)

cont = 0
for i in range(linhas):
    for j in range(colunas):
        matrix[i][j] = vetor[cont]
        cont+=1


ponto_de_consulta = []
for i in range(colunas-1):
    ponto_de_consulta.append(float(input("Digite as coordenadas ponto de consulta: ")))
k = int(input("Digite a quantidade de vizinhos proximos: "))


"""
    Calculo da distancia euclidiana
"""
E = []
x = 0
for i in range(linhas):
    for j in range(colunas-1):
        valor = pow(ponto_de_consulta[j] - matrix[i][j], 2)
        x+= valor
        if(j == (colunas-2)):
            E.append(math.sqrt(x))
    x=0

"""
    Ordenando os resultados
"""
N = sorted(E)

"""
    Descobrindo o id da linha dos vizinhos mais próximos
"""
ids = []
for i in range(k):
    for j in range(linhas):
        if( N[i] == E[j]):
            ids.append(j)

"""
    Imprimindo os resultados
"""
for i in range(k):
    print(matrix[ids[i]][colunas-1])







 





