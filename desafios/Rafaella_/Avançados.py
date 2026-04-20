# 1
nome_completo = input("Digite seu nome completo: ")
nomes = nome_completo.split()

primeiro = nomes[0]
ultimo = nomes[-1]

print(f"Primeiro nome: {primeiro}")
print(f"Último nome: {ultimo}")

#2
numero = float(input("Digite um número: "))
if numero % 2 == 0:
    print(f"O número {numero} é PAR.")
else:
    print(f"O número {numero} é ÍMPAR.")

#3
print("=CALCULADORA RUDIMENTAR =")
print("Operações disponíveis: + , - , * , /")

operacao = input("Qual operação deseja realizar? ")
n1 = float(input("Digite o primeiro valor: "))
n2 = float(input("Digite o segundo valor: "))

#lógica do cálculo
if operacao == "+":
    resultado = n1 + n2
    print(f"Resultado: {n1} + {n2} = {resultado}")

elif operacao == "-":
    resultado = n1 - n2
    print(f"Resultado: {n1} - {n2} = {resultado}")

elif operacao == "*":
    resultado = n1 * n2
    print(f"Resultado: {n1} * {n2} = {resultado}")

elif operacao == "/":
    #caso for divido por 0
    if n2 != 0:
        resultado = n1 / n2
        print(f"Resultado: {n1} / {n2} = {resultado}")
    else:
        print("Erro: Não é possível dividir por zero!")

else:
    print("Operação inválida! Tente usar + , - , * ou /")