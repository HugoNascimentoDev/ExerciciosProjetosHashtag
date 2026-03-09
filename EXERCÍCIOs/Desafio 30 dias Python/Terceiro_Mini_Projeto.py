def linha (tamanho):
    print('-' * tamanho)

def cabecalho(texto):
    linha(50)
    print(texto.center(50))
    linha(50)

from time import sleep
from random import randint

def jogada_computador ():
    jogada_pc = randint(1, 3)
    return jogada_pc

def menu ():
    cabecalho('ESCOLHA UMA OPÇÃO:')
    print('''[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA''')
    linha(50)

    while True:
        try:
            opcao = int(input('Qual a sua jogada? 1, 2 ou 3?   '))
            if opcao in [1, 2, 3]:
                return opcao
            else:
                print('Digite um valor válido!!! ')
        except:
            print('Digite um valor válido!!! ')
            
        

lista_de_jogadas = ['PEDRA', 'PAPEL','TESOURA']

def jogada(lista, humano, jogada_pc):
    cabecalho('JOGANDO...')
    print('JO...'.center(50))
    sleep(0.5)
    print('KEN...'.center(50))
    sleep(0.5)
    print('PO!!!'.center(50))
    sleep(0.5)
    cabecalho('RESULTADO...')
    status_jogada = 0
    # status_jogada = 1 -> EMPATE
    # status_jogada = 2 -> JOGADOR VENCEU
    # status_jogada = 3 -> PC VENCEU
    if humano == jogada_pc:
        print(f'JOGADOR escolheu: {lista[humano-1]}')
        print(f'COMPUTADOR escolheu: {lista[jogada_pc-1]}')
        cabecalho('JOGO EMPATADO!!!')
        status_jogada = 1
    else:
        if humano == 1 and jogada_pc == 3 or humano == 2 and jogada_pc == 1 or humano == 3 and jogada_pc == 2:
            print(f'JOGADOR escolheu: {lista[humano-1]}')
            print(f'COMPUTADOR escolheu: {lista[jogada_pc-1]}')
            cabecalho('PARABÉNS!!! JOGADOR VENCEU')
            status_jogada = 2
        else:
            print(f'JOGADOR escolheu: {lista[humano-1]}')
            print(f'COMPUTADOR escolheu: {lista[jogada_pc-1]}')
            cabecalho('NÃO FOI DESTA VEZ!!! COMPUTADOR VENCEU!!!')
            status_jogada = 3
    return status_jogada
    
def placar (empate, jogador_vence, pc_vence):
    cabecalho('PLACAR')
    print(f'EMPATE: {empate}')
    print(f'JOGADOR: {jogador_vence}')
    print(f'COMPUTADOR: {pc_vence}')
    linha(50)

# Programa Principal

empate = 0
jogador_vence = 0
pc_vence = 0

while True:
    cabecalho('VAMOS JOGAR??? JO KEN PO !!!')
    jogada_humana = menu()
    jogada_pc = jogada_computador()
    status_jogada = jogada(lista_de_jogadas, jogada_humana, jogada_pc)
    if status_jogada == 1:
        empate += 1
    elif status_jogada == 2:
        jogador_vence += 1
    else:
        pc_vence += 1
    placar(empate, jogador_vence, pc_vence)
    continuar = ' '
    while continuar not in 'NS':
        continuar = input('VAMOS JOGAR MAIS UMA VEZ ??? [S/N] ').upper().strip()
    if continuar == 'N':
        placar(empate, jogador_vence, pc_vence)
        cabecalho('VOLTE SEMPRE!!!')
        break

        


