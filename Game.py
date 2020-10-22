from Player import Player
from House import House
from Room import Room
from commands import Commands

import sys


class Game:        
        
        def __init__(self, house, player, commands):
                self.house=house
                self.player=player
                self.commands=commands
                self.play()
                   

        def promt(self):
                return input().strip().split(" ")

        def play(self):
                print("Welcome to the House Game. \n You are in the Hall. \n There is door N.")
                while True:
                        Input = self.promt()
                        if Input[0] not in self.commands.command_dict or len(Input) not in [1,2]:
                                self.commands.guidePlayer()

                        if Input[0]=="go" and len(Input)>1:
                                print(self.commands.goC(Input))

                        if Input[0]=="take" and len(Input)>1:
                                self.commands.takeC(Input)

                        if Input[0]=="release" and len(Input)>1:
                                self.commands.releaseC(Input)

                        if Input[0]=="unlock" and len(Input)>1:
                                print(self.commands.unlockC(Input))

                        if Input[0]=="show" and len(Input)==1:
                                print(self.commands.showC(Input))

                        if Input[0]=="commands" and len(Input)==1:
                                print(self.commands.commandsC(Input))

                        if Input[0]=="holding" and len(Input)==1:
                                self.commands.holdingC(Input)

                        if Input[0]=="read" and len(Input)>1:
                                print(self.commands.readC(Input))

                        if Input[0]=="open" and len(Input)>1:
                                print(self.commands.openC(Input))

                        if Input[0]=="quit" and len(Input)==1: 
                                print(self.commands.quitC(Input))
                        
        
         
    
##START GAME##


GameInstance=Game(House(sys.argv[1]), Player(), Commands())









 

    

