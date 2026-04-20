import random

def jogar():
    while True:
        # Configurações iniciais
        numero_secreto = random.randint(0, 10)
        tentativas_totais = 5
        pontuacao = 0
        acertou = False
        
        print("\n" + "="*30)
        print("  JOGO DE ADIVINHAÇÃO (0 a 10)  ")
        print("="*30)
        print(f"Você tem {tentativas_totais} tentativas. Boa sorte!")

        for tentativa in range(1, tentativas_totais + 1):
            try:
                chute = input(f"\nTentativa {tentativa} - Digite um número: ")
                chute = int(chute)
                
                if chute < 0 or chute > 10:
                    print("AVISO: O número deve estar entre 0 e 10!")
                    continue # Não gasta tentativa se o número for fora da faixa
            except ValueError:
                print("ERRO: Digite apenas números inteiros!")
                continue 

            if chute == numero_secreto:
                pontuacao = 100 - ((tentativa - 1) * 22.5) 
                
                print(f"PARABÉNS! Você acertou o número {numero_secreto}!")
                print(f"Sua pontuação final: {int(pontuacao)} pontos.")
                acertou = True
                break
            elif chute < numero_secreto:
                print("Tente um número MAIOR...")
            else:
                print("Tente um número MENOR...")

        if not acertou:
            print("\n" + "x"*30)
            print(f"GAME OVER! O número era {numero_secreto}.")
            print("Pontuação: 0 pontos.")
            print("x"*30)

        # Opção de nova partida
        denovo = input("\nDeseja jogar novamente? (S/N): ").strip().upper()
        if denovo != 'S':
            print("Obrigado por jogar! Até a próxima.")
            break

# Inicia o programa
jogar()
