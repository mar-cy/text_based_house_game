
class Room():
    
    def __init__(self):
        self.content=["table", "key", "chair", "bag", "book"]    #list for items that are in the rooms (and not with the player)

        
    def showItems(self):
        if self.content==[]:
            return "There is nothing to show."
        else:
            return "Available items:  " + ",".join(self.content)


    def removeItem(self, item):
        self.content.remove(item)
        

    def addItem(self, item):
        self.content.append(item)
