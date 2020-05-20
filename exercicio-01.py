# -*- coding: utf-8 -*-
"""
Created on Sun May 10 16:53:23 2020

@author: eltes
"""

'''
Exercício 01. 
Dadas as seguintes séries temporais
    • s1 = 168, 398, 451, 337, 186, 232, 262, 349, 189, 204, 220, 220, 207, 239, 259, 258,
242, 331, 251, 323, 106, 1055, 170

    • s2 = 168, 400, 451, 300, 186, 200, 262, 349, 189, 204, 220, 220, 207, 239, 259, 258,
242, 331, 251, 180, 106, 1055, 200

Utilize funções NumPy para:
• calcular a distância euclidiana entre as séries
• calcular a série temporal com os valores médios entre s1 e s2
• calcular a série temporal com os valores máximos de cada instante entre s1 e s2
• calcular a série temporal com os valores mínimos de cada instante entre s1 e s2
'''

import numpy as np


s1 = (168, 398, 451, 337, 186, 232, 262, 349, 189, 204, 220, 220, 207, 239, 259, 258,
242, 331, 251, 323, 106, 1055, 170)

s2 = (168, 400, 451, 300, 186, 200, 262, 349, 189, 204, 220, 220, 207, 239, 259, 258,
242, 331, 251, 180, 106, 1055, 200)

s1_array = np.array((s1)) # convertendo a lista s1 para array
s2_array = np.array((s2)) # convertendo a lista s2 para array

# Cálculo da Distância Euclidiana
dst = np.linalg.norm(s1_array - s2_array)

# visualizando o resultado
print("s1: "+ str(s1) + "\n\n" + "s2" + str(s2))
print()
print("The Euclidean distance(s1,s2) is:",dst)

# calculo série temporal com os valores médios entre s1 e s2 
s_mean= np.mean(np.array([s1_array,s2_array]),axis=0) # Ver referência 1 abaixo
print("\nMean values: " + str(s_mean))

# calculo série temporal com os valores máximos de cada instante entre s1 e s2
s_max = np.maximum(s1_array,s2_array)
print("\nMaximum values: " + str(s_max))

# calculo série temporal com os valores mínimos de cada instante entre s1 e s2
s_min = np.minimum(s1_array,s2_array)
print("\nMinimum values: " + str(s_min))

# Referência 1
# https://stackoverflow.com/questions/19886584/calculate-mean-of-arrays-in-numpy
