# -*- coding: utf-8 -*-
"""
Created on Sun May 10 16:53:23 2020

@author: eltes
"""

'''
Exercício 02. A Tabela 1, extraída do portal do IBGE, apresenta a distribuição da
população por sexo, segundo os grupos de idade no Brasil, para o ano de 2010. Com
base nesta tabela, construa um gráfico de barras vertical com os dados da distribuição da
população feminina.
'''

import numpy as np
import matplotlib.pyplot as plt

idade = ("0 a 4 anos", "5 a 9 anos", "10 a 14 anos", "15 a 19 anos", "20 a 24 anos", "25 a 29 anos",
         "30 a 34 anos", "35 a 39 anos", "40 a 44 anos", "45 a 49 anos", "50 a 54 anos", "55 a 59 anos",
         "60 a 64 anos", "65 a 69 anos", "70 a 74 anos", "75 a 79 anos", "80 a 84 anos",
         "85 a 89 anos", "90 a 94 anos", "95 a 99 anos", "100 anos e mais")

pop_fem = (6779171, 7345231, 8441348, 8432004, 8614963, 8643419, 8026854, 7121915,
           6688796, 6141338, 5305407, 4373877, 3468085, 2616745, 2074264, 1472930,
           998349, 508724, 211594, 66806, 16989)

x_pos = np.arange(len(idade))

plt.figure( figsize=(10, 5) )

plt.bar(x_pos, pop_fem, align='center',
        color='orange', linewidth=1, edgecolor='black')

plt.yticks([ 0, 2000000, 4000000, 6000000, 8000000,10000000 ],
           [ "0", "2", "4", "6 ", "8", "10" ] )

plt.xticks(x_pos, idade, rotation=45)

plt.xlabel('Faixa etária',fontweight="bold")
plt.ylabel('Número absoluto (em milhões)',fontweight="bold")
plt.title('Distribuição da População Feminina por faixa etária\n(IBGE: 2010)',fontweight="bold")

plt.grid(b=True, color='gray', linestyle='--', linewidth=0.5);

plt.show()

