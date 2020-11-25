# Disciplina: Probabilidade e Estatística
# Aluno: Paulo Vinicius Mota - 2014290074 - ADS Noturno
# Lista 5

import statistics #Importando modulo statistic para as formulas matematicas
l_con = [67,75,63,72,77,78,81,77,80]#Insersão dos dados a serem calculados a uma lista

soma = sum(l_con)#Soma de todos os valores
tam = len(l_con)#Quantidade de valores
md_arit = soma/tam#Média Aritmética dos valores
md_harm = statistics.harmonic_mean(l_con)#Adiciona a variavel o valor da media harmonica atraves do metodo harmonic_mean
md_geo = statistics.geometric_mean(l_con)#Adiciona a variavel o valor da media geometrica atraves do metodo geometric_mean 
moda = statistics.mode(l_con)#Adiciona a variavel o valor da moda atraves do metodo mode 
vari = statistics.pvariance(l_con)#Adiciona a variavel o valor da variancia atraves do metodo pvariance
devp = statistics.stdev(l_con)#Adiciona a variavel o valor do desvio padrao atraves do metodo stdev
print("Média Aritmética Simples: ",round(md_arit,2))#Imprimi a media aritmetica 
print("Média Harmonica:",round(md_harm,2))#Imprimi Media harmonica dos valores da lista 
print("Média Geométrica:",round(md_geo,2))#Imprimi media geometrica dos valores da lista 
print("Moda:",round(moda,2))#Imprime a moda dos valores da lista 
print("Variancia: ",round(vari,2))#Imprime variancia dos valores da lista 
print("Desvio Padrão: ",round(devp,2))#Imprime desvio padrao dos valores da lista 