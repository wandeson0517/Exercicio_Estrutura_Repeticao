# ==========================================
# QUESTÃO 7 
# =========================================
# ENUNCIADO: 
#  Faça um programa que leia 5 números e informe o maior número.
# ------------------------------------------------------------

num_maior = None

for i in range (5):
    num = float(input("Informe um numero: "))

    if num_maior == None:
        num_maior = num

    if num > num_maior:
       num_maior = num
print(f"O maior numero: {num_maior}")