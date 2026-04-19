# ==============================
# DESAFIOS PRÁTICOS PYTHON
# ==============================

# ----------- MENSAGENS -----------

# 1. Hello World
print("Hello World")

# 2. Saudação personalizada
nome = input("Digite seu nome: ")
print("Olá,", nome)


# ----------- NÚMEROS -----------

# 1. Número, antecessor e sucessor
num = int(input("Digite um número: "))
print("Número:", num)
print("Antecessor:", num - 1)
print("Sucessor:", num + 1)

# 2. Número com duas casas decimais
num2 = float(input("Digite um número: "))
print("Número formatado: {:.2f}".format(num2))

# 3. Média de 4 notas
notas = []
for i in range(4):
    nota = float(input("Digite uma nota: "))
    notas.append(nota)

media = sum(notas) / 4
print("Média:", media)

# 4. Par ou ímpar
numero = int(input("Digite um número: "))
if numero % 2 == 0:
    print("Par")
else:
    print("Ímpar")


# ----------- LISTAS -----------

# 1. Média, maior e menor nota
notas_lista = []
for i in range(4):
    nota = float(input("Digite uma nota: "))
    notas_lista.append(nota)

media_lista = sum(notas_lista) / 4
print("Média:", media_lista)
print("Maior nota:", max(notas_lista))
print("Menor nota:", min(notas_lista))

# 2. Aprovado ou reprovado
media2 = sum(notas_lista) / 4

if media2 >= 7:
    print("APROVADO")
else:
    prova_final = float(input("Digite a nota da prova final: "))
    nova_media = (media2 + prova_final) / 2
    if nova_media >= 5:
        print("APROVADO")
    else:
        print("REPROVADO")


# ----------- FUNÇÕES -----------

def par_ou_impar(n):
    if n % 2 == 0:
        return "Par"
    else:
        return "Ímpar"

teste = int(input("Digite um número: "))
print(par_ou_impar(teste))


# ----------- DICIONÁRIO -----------

dicionario = {'m1': {'m2': 'Olá Mundo'}}
print(dicionario['m1']['m2'])


# ----------- STRINGS -----------

frase = "Exercícios de Java"
nova_frase = frase.replace("Java", "Python")
print(nova_frase)


# ----------- DATAS -----------

from datetime import datetime, timedelta

data_atual = datetime.now()
print("Data atual:", data_atual.date())

futuro = data_atual + timedelta(days=2)
print("Data daqui a 2 dias:", futuro.date())


# ----------- AVANÇADO -----------

# 1. Primeiro e último nome
nome_completo = input("Digite seu nome completo: ").split()
print("Primeiro nome:", nome_completo[0])
print("Último nome:", nome_completo[-1])

# 2. Par ou ímpar (de novo)
num_av = int(input("Digite um número: "))
if num_av % 2 == 0:
    print("Par")
else:
    print("Ímpar")

# 3. Calculadora simples
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
op = input("Digite a operação (+, -, *, /): ")

if op == "+":
    print("Resultado:", n1 + n2)
elif op == "-":
    print("Resultado:", n1 - n2)
elif op == "*":
    print("Resultado:", n1 * n2)
elif op == "/":
    print("Resultado:", n1 / n2)
else:
    print("Operação inválida")


# ----------- MAP -----------

# 1. Celsius para Fahrenheit
celsius = [22.5, 40, 13, 29, 34]
fahrenheit = list(map(lambda c: (c * 9/5) + 32, celsius))
print("Fahrenheit:", fahrenheit)

# 2. Soma pares e ímpares
lista = [21, 5, 34, 8, 16, 7, 3]
pares = sum(x for x in lista if x % 2 == 0)
impares = sum(x for x in lista if x % 2 != 0)

print("Soma pares:", pares)
print("Soma ímpares:", impares)

# 3. Maior e menor valor
lista2 = [54, 10, 29, 87, 7, 64]
print("Maior:", max(lista2))
print("Menor:", min(lista2))


# ----------- PROJETO (JOGO) -----------

import random

def jogo():
    numero = random.randint(0, 10)
    tentativas = 5

    for i in range(tentativas):
        try:
            palpite = int(input("Adivinhe o número (0 a 10): "))
        except:
            print("Digite um número válido!")
            continue

        if palpite < 0 or palpite > 10:
            print("Número fora do intervalo!")
            continue

        if palpite == numero:
            pontos = 100 - (i * 20)
            print("Acertou! Pontos:", pontos)
            return
        else:
            print("Errou!")

    print("Você perdeu! O número era:", numero)

# repetir jogo
while True:
    jogo()
    repetir = input("Quer jogar novamente? (s/n): ")
    if repetir.lower() != 's':
        print("Fim do jogo")
        break