# ==========================================
# QUESTÃO 14
# =========================================
# ENUNCIADO: 
#  Faça um programa que peça 10 números inteiros, 
#  calcule e mostre a quantidade de números pares e a quantidade de números impares.
# ------------------------------------------------------------
contador_par = 0
contador_impar = 0

for i in range(10):
    num = int(input("Informe um numero inteiro: "))
    if num % 2 == 0:
        contador_par += 1
    else:
        contador_impar += 1
        
print(f"\nA Quantidade de numeros pares: {contador_par}")
print(f"\nA Quantidade de numeros pares: {contador_impar}")

