from House import House
from Player import Player
from Room import Room
from Com_Dict import Com_Dict

import sys

Housefile=sys.argv[1]
house=House(Housefile)
player=Player()
room=Room()
com_dict=Com_Dict()

class Commands(Com_Dict):
    def __init__(self):
        Com_Dict.__init__(self)
        
       
  
    def guidePlayer(self):
        print("Command invalid. Please choose one from the below ones", com_dict.printDict())


    def goC(self, command):
            for sublist in house.returnDoors():
                if sublist[0]==house.cur_location and sublist[1]==command[1]:
                    if sublist[2]=="open":
                        house.cur_location=sublist[3]
                        return house.returnRooms()[house.cur_location]    
                    elif sublist[2]=="closed":
                        return "The  door is closed."
                    else:
                        return "The door is locked."
                
                                                                        

    def takeC(self, command):
        if house.returnItems()[command[1]][0]==house.returnLocation() and house.returnItems()[command[1]][1]!="STATIONARY": #take item it has status USE or MOVE
            room.removeItem(command[1])
            return player.addInventory(command[1])
            
        else:
            print("You cannot take this item")
                            
            
    def releaseC(self, command):
        if command[1] in player.returnInventory():
            room.addItem(command[1])
            return player.removeInventory(command[1])  #release item from Player, add to Room content
        elif command[1] not in player.returnInventory() and player.returnInventory()!=[]:
            print("You do not have this item.")
        else:
            print("There are no items to be released.")


    def unlockC(self, command): 
        for sub in house.returnDoors():
            if sub[0]==house.returnLocation() and sub[1]==command[1]:
                if sub[2]=="locked":
                    if "key"in player.returnInventory():
                        sub[2]="open"
                        return "The door is now unlocked."
                    else:
                        return "You need a key to unlock the door."

                elif sub[2]=="open":
                    return "The door is open."
                elif sub[2]=="closed":
                    return "The door is closed."
      
        

            

            
    def showC(self, command):
        return house.returnRooms()[house.cur_location]
                    

    def commandsC(self, command):
        return [*self.command_dict]


    def holdingC(self, command):
        return player.showInventory()
                    

    def readC(self, command):
        if command[1] in player.inventory:
            return house.returnItems()[command[1]][3]
        else:
            return "No item to read."

    def openC(self, command):
        for sublist in house.returnDoors():
            if sublist[0]==house.returnLocation() and sublist[1]==command[1]:
                if sublist[2]=="closed":
                    sublist[2]="open"
                    return "The door has been opened."
                if sublist[2]=="open":
                    return "The door is already open."
                if sublist[2]=="locked":
                    return "The door is locked."
                else:
                    return "You have to be in the right room first" 
                                    
        
        
    def quitC(self, command):
        print("Good bye and thanks for playing.")
        sys.exit()
    
        


