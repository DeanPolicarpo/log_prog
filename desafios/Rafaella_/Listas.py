#1
notas= []
notas.append(float(input("Nota 1: ")))
notas.append(float(input("Nota 2: ")))
notas.append(float(input("Nota 3: ")))
notas.append(float(input("Nota 4: ")))

maior = max(notas)
menor = min(notas)
media = sum(notas)/ 4

print(f"Maior Nota: {maior}")
print(f"Menor Nota: {menor}")
print(f"Média Final: {media:.1f}")

#2
if media >= 7:
    print("APROVADO")
else:
    final = float(input("Nota da prova final: "))
    nova_media = (media + final) / 2
    print(f"Nova média: {nova_media:.1f}")
    
    if nova_media >= 5:
        print("APROVADO")
    else:
        print("REPROVADO")