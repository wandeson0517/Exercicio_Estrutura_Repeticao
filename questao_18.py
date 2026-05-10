# ==========================================
# QUESTÃO 18
# =========================================
# ENUNCIADO: 
#  Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor
#  e a soma dos valores.
# ------------------------------------------------------------

# 1. Definir quantos números serão lidos
try:
    n = int(input("Digite a quantidade de números (N): "))
    
    if n <= 0:
        print("Por favor, digite um número maior que zero.")
    else:
        numeros = []
        
        # 2. Ler os N números
        for i in range(n):
            valor = float(input(f"Digite o {i+1}º número: "))
            numeros.append(valor)
        
        # 3. Calcular e exibir resultados
        menor = min(numeros) # Encontra o menor
        maior = max(numeros) # Encontra o maior
        soma = sum(numeros)  # Soma os valores
        
        print("-" * 20)
        print(f"Conjunto de números: {numeros}")
        print(f"Menor valor: {menor}")
        print(f"Maior valor: {maior}")
        print(f"Soma dos valores: {soma}")
        print("-" * 20)

except ValueError:
    print("Entrada inválida. Por favor, digite números inteiros.")