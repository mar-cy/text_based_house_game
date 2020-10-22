import sys

Housefile=sys.argv[1]


class House:
    
    
    def __init__(self, Housefile):
        self.rooms={}  #dict, room as key, description of room as value
        self.doors=[]  #list that contains sublists with room name and possible directions
        self.items={}  #dict, item name as key, locatin,  usage, and further info as value       
        self.cur_location="Hall"

        with open(Housefile) as f:
            for line in f:
                line=line.rstrip("\n")
                line=line.split(" ")

                if line[0]=="room":                    
                    description=" ".join(line[2:])
                    description=description.rstrip()
                    self.rooms[line[1]]=description
            


                if line[0]=="door":
                    directions=line[1].rsplit("-")
                    Fdir, Bdir=directions[0], directions[1]
                    self.doors.append([line[3],Fdir,line[2], line[4]])
                    self.doors.append([line[4], Bdir, line[2], line[3]])
        
                if line[0]=="item":
                    if line[3]=="STATIONARY" or line[3]=="MOVE":
                        self.items[line[1]]=line[2], line[3]
                    elif line[3]=="USE":
                        Text=" ".join(line[5:])
                        self.items[line[1]]=line[2], line[3], line[4], Text
    def __str__(self):
        return Housefile


    def returnRooms(self):   
        return self.rooms 


    def returnDoors(self):
        return self.doors


    def returnItems(self):
        return self.items

    def returnLocation(self):
        return self.cur_location
               


    











































 
                        



              
                    
        





        


                    

                    
