from time import sleep
import os
os.system("cls")

print("-"*60)
print("{:^60}".format("QUIZ JÚNIOR"))
print("-"*60)

# nome = input("Qual o seu nome? ")
# print(f"Olá, {nome}!")
# resposta = input("Gostaria de iniciar o jogo? (S/N) ")
# resposta = resposta.upper()
# if resposta != "S":
#     print("Ok. Até a próxima!")
#     quit()
    
# print("Iniciando...")
# sleep(1)

#Perguntas
print("-"*15)
print("{:^15}".format("Questão 1"))
print("-"*15)
print("Quantos fusos horários existem na Rússia? \n a- 9 \n b- 18 \n c- 5 \n d- 11")
r1 = input("Resposta: ").lower()

while r1 != "a" and r1 != "b" and r1 != "c" and r1 != "d": 
    print("\033[31mResposta Inválida!\033[m")
    r1 = input("Insira resposta válida: ").lower()

print(".")
sleep(0.5)
print(".")
sleep(0.5)
print(".")
sleep(0.5)

if r1 == "d":
    print("\033[32mResposta Correta!\033[m")
else:
    print("\033[31mResposta Incorreta!\033[m")
