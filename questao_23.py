
# ================================================
# QUESTAO 23. 
# =================================================
# ENUNCIADO:
# Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário. 
# O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos. 
# Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados.
# --------------------------------------------------------------------------------------------

num = int(input('Digite um numero inteiro:' ))


for n in range(2, num+1):
    primo = True

    for i in range(2 ,n):
       if n % i == 0:
           primo = False
           break

if primo:
    print(f"{n} é primo!")
else:
    print(f"{n} não é primo.")