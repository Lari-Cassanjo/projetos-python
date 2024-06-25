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
    
print("-"*15)
print("{:^15}".format("Questão 2"))
print("-"*15)
print("Qual é o animal nacional da Austrália? \n a- Coala \n b- Canguru Vermelho \n c- Canguru Marrom \n d- Aranha Gigante")
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

if r1 == "b":
    print("\033[32mResposta Correta!\033[m")
else:
    print("\033[31mResposta Incorreta!\033[m")

print("-"*15)
print("{:^15}".format("Questão 3"))
print("-"*15)
print("Onde é o lugar natural mais baixo do planeta Terra? \n a- Fossa de Java \n b- Mar Jônico \n c- Fossa das Marianas \n d- Mar Morto")
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

if r1 == "c":
    print("\033[32mResposta Correta!\033[m")
else:
    print("\033[31mResposta Incorreta!\033[m")

print("-"*15)
print("{:^15}".format("Questão 4"))
print("-"*15)
print("Qual país tem mais ilhas no mundo? \n a- Suécia \n b- Nova Zelândia \n c- Austrália \n d- Finlândia")
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

if r1 == "a":
    print("\033[32mResposta Correta!\033[m")
else:
    print("\033[31mResposta Incorreta!\033[m")

print("-"*15)
print("{:^15}".format("Questão 5"))
print("-"*15)
print("Qual é a série de livros mais vendida do século 21? \n a- Bíblia \n b- Harry Potter \n c- Percy Jackson \n d- After")
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

if r1 == "b":
    print("\033[32mResposta Correta!\033[m")
else:
    print("\033[31mResposta Incorreta!\033[m")

print("-"*15)
print("{:^15}".format("Questão 6"))
print("-"*15)
print("Qual artista pintou o teto da Capela Sistina, em Roma? \n a- Leonardo da Vinci \n b- Michelangelo Buonarroti \n c- Donato di Niccoló \n d- Rafael Sanzio")
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

if r1 == "b":
    print("\033[32mResposta Correta!\033[m")
else:
    print("\033[31mResposta Incorreta!\033[m")

print("-"*15)
print("{:^15}".format("Questão 7"))
print("-"*15)
print("O que aconteceu em 20 de Julho de 1969? \n a- O Sputnik entrou em órbita \n b- A Laika foi ao Espaço \n c- Yuri Gagarin disse que a Terra é azul \n d- Apollo 11 pousou na lua")
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

print("-"*15)
print("{:^15}".format("Questão 8"))
print("-"*15)
print("Quando o metrô de Londres foi inaugurado? \n a- 1863 \n b- 1875 \n c- 1822 \n d- 1899")
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

if r1 == "a":
    print("\033[32mResposta Correta!\033[m")
else:
    print("\033[31mResposta Incorreta!\033[m")

print("-"*15)
print("{:^15}".format("Questão 9"))
print("-"*15)
print("Quantas teclas há em um piano clássico? \n a- 84 \n b- 82 \n c- 88 \n d- 86")
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

if r1 == "c":
    print("\033[32mResposta Correta!\033[m")
else:
    print("\033[31mResposta Incorreta!\033[m")

print("-"*15)
print("{:^15}".format("Questão 10"))
print("-"*15)
print("Quando a Netflix foi fundada? \n a- 1997 \n b- 2001 \n c- 2009 \n d- 2015")
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

if r1 == "a":
    print("\033[32mResposta Correta!\033[m")
else:
    print("\033[31mResposta Incorreta!\033[m")

