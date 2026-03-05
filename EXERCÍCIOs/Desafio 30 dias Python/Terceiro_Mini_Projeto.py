def linha (tamanho = 50):
    print('-' * tamanho)

def cabecalho(texto):
    linha(50)
    print(texto.center(50))
    linha(50)

def menu (opcao = 0):
    cabecalho('ESCOLHA UMA OPÇÃO:')
    print('''[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA''')
    linha(50)
    opcao= int(input('Qual a sua jogada? 1, 2 ou 3?'))
    linha(50)    

from time import sleep
from random import randint

def jogada 


cabecalho('VAMOS JOGAR??? JO KEN PO !!!')
menu()
