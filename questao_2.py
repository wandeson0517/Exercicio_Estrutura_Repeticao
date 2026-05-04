# ==========================================
# QUESTÃO 2
# =========================================
# ENUNCIADO: 
#  2. Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário,
#  mostrando uma mensagem de erro e voltando a pedir as informações.
# ------------------------------------------------------------

while True:
    nome = (input("Informe um nome de um usuario: "))
    senha = (input("Informe uma senha: "))
    if nome == senha:
        print(f"Seu {nome} e sua {len(senha) * "*"} são IGUAIS. Tente Novamente.👍")
    else:
        print(f"Seu nome {nome} e sua senha {len(senha) * "*"} são DIFERENTES: Acesso Permitido!")
        break
print("== Fim do Programa ==")