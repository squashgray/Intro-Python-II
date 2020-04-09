
class Player:
    def __init__(self,name, current_room):
        self.name = name
        self.current_room = current_room

    def __str__(self):
        return f"PLAYER: {self.name}\nLOCATION: {self.current_room}"

    def move(self,direction):
        if getattr(self.current_room, f"{direction}_to"):
            self.current_room = getattr(self.current_room, f"{direction}_to")
            print(f"\n{self.name} has entered the {self.current_room.name}\n"
                f"You look around and observe, {self.current_room.description}\n")            
        else:
            print(f"You hit a wall, choose different direction\n")
