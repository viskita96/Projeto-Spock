# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 18:05:42 2015

@author: vitorkitahara
"""
import random
list = ["pedra","papel","spock","lagarto","tesoura"]

play = True
while play == True:
    pcs=0
    pls=0
    play = False
    while pcs<3 and pls<3:
        pc = random.choice(list)
        player=str(input("Digite a sua jogada, por favor \n"))
        print("O computador jogou:" + pc)
        
        if pc=="pedra" and (player=="tesoura" or "lagarto"):
            pcs+=1
            print('Computador ganhou a rodada \n Computador ', pcs, ', Jogador ' ,pls)
        elif player=="pedra" and (pc=="tesoura" or pc=="lagarto"):
            pls+=1
            print('Você ganhou a rodada \n Computador ', pcs ,', Jogador ' ,pls)
        elif pc=="papel" and (player=="pedra" or pc=="spock"):
            pcs+=1
            print('Computador ganhou a rodada \n Computador ', pcs, ', Jogador ' ,pls)
        elif player=="papel"and (pc=="pedra" or pc=="spock"):
            pls+=1
            print('Você ganhou a rodada \n Computador ', pcs ,', Jogador ' ,pls)
        elif pc=="spock" and (player=="pedra" or pc=="tesoura"):
            pcs+=1
            print('Computador ganhou a rodada \n Computador ', pcs, ', Jogador ' ,pls)
        elif player=="spock" and (pc=="pedra" or pc=="tesoura"):
            pls+=1
            print('Você ganhou a rodada \n Computador ', pcs ,', Jogador ' ,pls)
        elif pc=="lagarto" and (player=="papel" or pc=="spock"):
            pcs+=1
            print('Computador ganhou a rodada \n Computador ', pcs, ', Jogador ' ,pls)
        elif player=="lagarto" and (pc=="papel" or pc=="spock"):
            pls+=1
            print('Você ganhou a rodada \n Computador ', pcs ,', Jogador ' ,pls)
        elif pc=="tesoura" and (player=="papel" or pc=="lagarto"):
            pcs+=1
            print('Computador ganhou a rodada \n Computador ', pcs, ', Jogador ' ,pls)
        elif player=="tesoura" and (player=="papel" or pc=="lagarto"):
            pls+=1
            print('Você ganhou a rodada \n Computador ', pcs ,', Jogador ' ,pls)
        elif player == pc:
            print('Deu empate, jogue novamente \n Computador ', pcs ,', Jogador ' ,pls)
        else:
            print('Voce escreveu algo errado, digite novamente')
