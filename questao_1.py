# ==========================================
# QUESTÃO 1
# =========================================
# ENUNCIADO: 
#  1. Faça um programa que peça uma nota, entre zero e dez. 
# Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.
# ------------------------------------------------------------


while True:
    num = int(input("Informa uma nota entre 0 a 10: "))
    if num < 0 or num > 10:
        print(f"O numero informado n°{num} é Invalido! Tente novamente.")
        
    else:
        print(f"O numero informado n°{num} é  Valido!")
        break
print("---Fim do Programa---")