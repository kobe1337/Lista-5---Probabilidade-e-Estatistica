# Disciplina: Probabilidade e Estatística
# Aluno: Paulo Vinicius Mota - 2014290074 - ADS Noturno
# Lista 5

import statistics

l_dados= [4.0,4.5,5.0,5.0,5.5,6.0,6.0,6.5,6.5,6.5,6.5,7.0,7.0,7.0,7.0,7.0,7.0,7.5,8.5,9.0,9.0,9.0,9.5,10.0,10.0,10.5,11.0,12.0,12.5,13.0,13.0,]#Insersão dos dados a serem calculados a uma lista

devp = statistics.stdev(l_dados)#Adiciona a variavel o valor do desvio padrao atraves do metodo stdev
md_arit = statistics.mean(l_dados)#Adiciona a variavel o valor da media aritmética atraves do metodo md_arit
coe_var = devp/md_arit*100;#Adiciona a variavel o resultado do calculo de coeficiente de variação

print("Coeficente de Variação dos valores da lista: ",round(coe_var,3))#Imprimi o valor do coeficiente de variação dos valores da lista
