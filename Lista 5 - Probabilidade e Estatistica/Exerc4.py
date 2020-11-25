# Disciplina: Probabilidade e Estatística
# Aluno: Paulo Vinicius Mota - 2014290074 - ADS Noturno
# Lista 5
import statistics

l_prod = [12,15,18,22,17,17,18,23,29,12]#Insersão dos dados a serem calculados a uma lista
md_arit = statistics.mean(l_prod)#Adiciona a variavel o valor da media aritmética atraves do metodo mean
medi = statistics.median(l_prod)#Adiciona a variavel o valor da mediana atraves do metodo median
devp = statistics.pstdev(l_prod)#Adiciona a variavel o valor do desvio padrão atraves do metodo pstdev

print("Valor da produção média: ",round(md_arit,2))#Imprimi valor da produção media dos valores da lista
print("Valor da mediana da produção: ",round(medi,2))#Imprimi o valor da mediana da produção dos valores da lista
print("VAlor do desvio padrão: ",round(devp,2))#Imprimi o valor do desvio padrão da produção dos valores da lista
