# ==========================================
# QUESTÃO 8
# =========================================
# ENUNCIADO: 
#  8. Faça um programa que leia 5 números e informe a soma e a média dos números.
# ------------------------------------------------------------

soma = 0
media = 0

for i in range(5):
    num = int(input("Informe um numero: "))
    soma += num
media = soma / 5   

print(f"A soma dos numeros informados corresponde: {soma}")
print(f"A media dos numeros informados corresponde: {media}")