# [PY-A01]
# Faça um programa em python que determine em duas variáveis (senha e email) 
# e que contenha uma senha e um email cadastrados antecipadamente, em seguida 
# solicite ao usuário uma senha e um email e utilize o laço de repetição 
# juntamente com a estrutura de condição para verificar se o email e a senha 
# digitado pelo usuário é igual ao email e senha cadastrados antecipadamente. 
# E enquanto a senha e o email que o usuário digitou não for igual ao email e 
# senha cadastrados ele continue em um loop.

def ln(x):
    print("-"*x)

email = "auridebson@vutus.com"
senha = "abs23fta"

ln(30)
print("Verificação de email e senha")
ln(30)

login = input(f"Digite seu login(e-mail): ")
pwd = input(f"Agora digite sua senha: ")

ln(30)

while True:
    if login != email or pwd != senha:
        print(f"ERROR:\nEmail ou senha errados, tente novamente!")
        login = input(f"Digite seu login(e-mail): ")
        pwd = input(f"Agora digite sua senha: ")
    else:
        ln(30)
        print(f"INFO:\nVocê está logado no sistema!")
        ln(30)
        break

# Não coloquei conversão de case pois como se trata de
# login e senha, o case é considerado.