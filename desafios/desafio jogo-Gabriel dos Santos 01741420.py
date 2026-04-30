import random

def jogar():
    numero_secreto = random.randint(0, 10)
    tentativas_restantes = 5
    
    print("Bem-vindo ao Jogo de Adivinhação!")
    print("Eu escolhi um número entre 0 e 10. Você tem 5 tentativas para acertar.")

    while tentativas_restantes > 0:
        print(f"Tentativas restantes: {tentativas_restantes}")
        
        try:
            palpite = int(input("Digite seu palpite: "))
          
            if palpite == numero_secreto:
                print(f"Parabéns! Você acertou! O número era {numero_secreto}.")
                break
            elif palpite < numero_secreto:
                print("Muito baixo! Tente um número maior.")
            else:
                print("Muito alto! Tente um número menor.")
                
            tentativas_restantes -= 1
            
        except ValueError:
            print("Entrada inválida! Por favor, digite um número inteiro.")


    if tentativas_restantes == 0:
        print(f"Game Over! Suas tentativas acabaram. O número era {numero_secreto}.")

if __name__ == "__main__":
    jogar()