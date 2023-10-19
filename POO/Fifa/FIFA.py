from FifaClasses import *

while True:
    print("MENU")
    opcao = input(" [1]- Cadastrar Time  \n [2]- Cadastrar Jogador  \n [3]- Cadastrar Comissão Técnica  \n [4]- Sair  \n")

    if (opcao == '1'):
        nomeTime = input('Digite o nome do time:')
        cidade = input('Digite o cidade do time:')
        mascote = input('Digite o mascote do time:')
        print(time.__dict__)
        time = CadastroTime(nomeTime,cidade,mascote)
    
    elif opcao == '2':
        nomeJogador = input('Digite o nome do jogador:')
        nomeTime = input('Digite o nome do time:')
        numeroCamisa = input('Digite o número da camisa:')
        print(jogador.__dict__)
        jogador = CadastroJogador(nomeJogador, cidade, mascote)

    elif opcao == '3':
       opcao2 = input("[A]- Cadastrar Tecnico \n [B]- Cadastrar Auxiliar \n [C]- Cadastrar Preparador Fisico").upper()
       if opcao2 == 'A':
            nomeTecnico = input('Digite o nome do técnico: ')
            nomeTime = input('Digite o nome do time:')
            esquemaTatico = input('Digite o esquema tático: ')
            tecnico = Tecnicos(nomeTecnico, nomeTime, esquemaTatico)
            print(tecnico.dar_coletiva())
            print(tecnico.__dict__)

       elif opcao2 == 'B':
            nomeAuxiliar = input('Digite o nome do auxiliar: ')
            nomeTime = input('Digite o nome do time:')
            esquemaTatico = input('Digite o esquema tático: ')
            auxiliar = Auxiliares(nomeAuxiliar, nomeTime, esquemaTatico)
            print(auxiliar.dar_coletiva())
            print(auxiliar.__dict__)

       elif opcao2 == 'C':
            nomePreparador = input('Digite o nome do preparador: ')
            nomeTime = input("Informe o nome do time: ")
            preparar = input("Qual parte do elenco ele prepara? \n Jogadores de Linha ou Goleiros?")
            esquemaTatico = ''
            preparador = PreparadoresFisicos(nomePreparador, nomeTime,preparar,esquemaTatico)
            print(preparador.dar_coletiva())
            print(preparador.__dict__)
       else:
           print("Opção Inválida")

    elif(opcao == '4'):
        print("Saindo...")
        print(" ")
        print('=' * 30)
        break

    else:
        print("Opção Inváida!!")
       

        
            
        

        
           

    
