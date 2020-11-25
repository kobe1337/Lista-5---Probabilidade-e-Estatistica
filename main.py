# Disciplina: Probabilidade e Estatística
# Aluno: Paulo Vinicius Mota - 2014290074 - ADS Noturno
# Lista 5

import statistics #Importando modulo statistic para as formulas matematicas
l_con = [10,13,17,9,8,11,13,7]# Lista dos valores de consumo de sal

soma = sum(l_con)#Soma de todos os valores
tam = len(l_con)#Quantidade de valores
md_arit = soma/tam#Média Aritmética dos valores

print("Média Aritmética Simples: ",md_arit)#Imprimi a media aritmetica 
print("Média Harmonica:",statistics.harmonic_mean(l_con))#Imprimi Media harmonica dos valores da lista atraves do metodo harmonic_mean
print("Média Geométrica:",statistics.geometric_mean(l_con))#Imprimi media geometrica dos valores da lista atraves do metodo geometric_mean 
print("Moda:",statistics.mode(l_con))#Imprime a moda dos valores da lista atraves do metodo mode 
print("Variancia: ",statistics.pvariance(l_con))#Imprime variancia dos valores da lista atraves do metodo pvariance
print("Desvio Padrão: ",statistics.stdev(l_con))#Imprime desvio padrao dos valores da lista atraves do metodo stdev