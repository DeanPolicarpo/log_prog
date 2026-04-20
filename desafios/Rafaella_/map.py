#1
celsius = [22.5, 40, 13, 29, 34]
fahrenheit = [(c * 1.8) + 32 for c in celsius]
print("Conversões:")

for i in range(len(celsius)):
    print(f"{celsius[i]}°C  ->  {fahrenheit[i]:.1f}°F")
    
#2
numeros = [21, 5, 34, 8, 16, 7, 3]
soma_pares = 0
soma_impares = 0

for num in numeros:
    if num % 2 == 0:
        soma_pares += num
    else:
        soma_impares += num

print(f"Soma dos valores PARES: {soma_pares}")
print(f"Soma dos valores ÍMPARES: {soma_impares}")

#3
numeros = [54, 10, 29, 87, 7, 64]
maior = max(numeros)
menor = min(numeros)

print(f"Sequência: {numeros}")
print(f"O MAIOR valor é: {maior}")
print(f"O MENOR valor é: {menor}")
