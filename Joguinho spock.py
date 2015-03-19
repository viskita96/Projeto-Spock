# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 18:05:42 2015

@author: vitorkitahara
"""
import random
list = ["pedra","papel","spock","lagarto","tesoura"]

pcs=0
pls=0
play = True
while play == True:
    play = False
    while pcs<3 and pls<3:
        pc = random.choice(list)
        player=str(input("Digite a sua jogada, por favor \n"))
        print("O computador jogou:" + pc)
        
        if pc=="pedra" and (player=="tesoura" or "lagarto"):
            pcs+=1
            print('Computador ganhou a rodada \n Computador ', pcs, ', Jogador ' ,pls)
        elif player=="pedra" and (pc=="tesoura" or "lagarto"):
            pls+=1
            print('Você ganhou a rodada \n Computador ', pcs ,', Jogador ' ,pls)
        elif pc=="papel" and (player=="pedra" or "spock"):
            pcs+=1
            print('Computador ganhou a rodada \n Computador ', pcs, ', Jogador ' ,pls)
        elif player=="papel"and (pc=="pedra" or "spock"):
            pls+=1
            print('Você ganhou a rodada \n Computador ', pcs ,', Jogador ' ,pls)
        elif pc=="spock" and (player=="pedra" or "tesoura"):
            pcs+=1
            print('Computador ganhou a rodada \n Computador ', pcs, ', Jogador ' ,pls)
        elif player=="spock" and (pc=="pedra" or "tesoura"):
            pls+=1
            print('Você ganhou a rodada \n Computador ', pcs ,', Jogador ' ,pls)
        elif pc=="lagarto" and (player=="papel" or "spock"):
            pcs+=1
            print('Computador ganhou a rodada \n Computador ', pcs, ', Jogador ' ,pls)
        elif player=="lagarto" and (pc=="papel" or "spock"):
            pls+=1
            print('Você ganhou a rodada \n Computador ', pcs ,', Jogador ' ,pls)
        elif pc=="tesoura" and (player=="papel" or "lagarto"):
            pcs+=1
            print('Computador ganhou a rodada \n Computador ', pcs, ', Jogador ' ,pls)
        elif player=="tesoura" and (player=="papel" or "lagarto"):
            pls+=1
            print('Você ganhou a rodada \n Computador ', pcs ,', Jogador ' ,pls)
        elif player == pc:
            print('Empate \n Computador ', pcs ,', Jogador ' ,pls)
        else:
            print('Voce escreveu algo errado, digite novamente')
        
