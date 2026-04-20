#1
num= int(input("Digite um número inteiro: "))
su= num +1
ant= num -1

print(f'Número sucessor: {su}')
print(f'Número antecessor: {ant}')

#2
num= int(input("Digite outro número inteiro: "))
print(f'O número inteiro é: {num:.2f}')

#3
n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))
n4 = float(input("Digite a quarta nota: "))

notas= [n1, n2, n3, n4]
media= sum(notas)/ 4
print(f'A média final é: {media:.1f}')