from time import sleep #importei a função sleep , pra dar uma pequena pausa.
from random import randint# importei a função random pra gerar um numero aleatorio de 1 a 6
try:
    print("="*10 , "Simulador de DADO", "="*10)

    print("Você deseja Jogar o dado?")#um print perguntando se o usuario quer gerar o numero ou não
    usuario = str(input("Responda 'S' para Sim ou 'N' para não:\n"))#um imput pra pegar a resposta do usuario

###se a resposta do usuario for igual a Sim , vai ser gerado um numero de 1 a 6 e dps será printado na tela o mesmo.
###se a resposta for não o codigo ira encerrar.
###criei um loop com while pra caso a resposta for sim , o programa perguntar se o usuario quer gerar outro numero ou
#não

    if usuario == 's':
        n = randint(1,6)
        print('Jogando o Dado....')
        sleep(3)
        print(f'o numero foi {n}')
        while True:
            sleep(2)
            print("Você deseja Jogar outra vez?")
            sleep(1)
            usuario2 = input("Responda 'S' para Sim ou 'N' para não:\n")
            sleep(1)
            if usuario2 == "s":
                n2 = randint(1, 6)
                print('Jogando Dado....')
                sleep(3)
                print(f'o numero foi {n2}')
            else:
                break
    else:
        pass
except:
    print('erro!!!')
print("Programa Finalizado!!!!")
