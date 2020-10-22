class Com_Dict:

    def __init__(self):
        self.command_dict={"go":"to go from one room to another when a door is open", "open":"to open a closed door", "quit":"to quit the game", "holding":"to show what items the player is holding", "take":"to take an item and put it in player's inventory", "release":"to remove an item from Player's inventory and put it in the current room", "commands":"to list all possible commands", "show":"to show current location, possible directions and any existing items", "unlock":"to unlock a locked door", "read": "to read content from the item book"}

    def printDict(self):
        return self.command_dict