class Player:
    def __init__(self):
        self.inventory=[]


    def returnInventory(self):
        return self.inventory

    def addInventory(self, item):
        self.inventory.append(item)
        print("You took" ,item, "successfully")      
    

    def removeInventory(self, item):
        self.inventory.remove(item)
        print("You released" ,item, "successfully.")

        

    def showInventory(self):
        if self.inventory==[]:
            print("You are holding no items.")        
        else:
            print("You are holding the following:", ",".join(self.inventory))
    

        
