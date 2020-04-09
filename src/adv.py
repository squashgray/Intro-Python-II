from room import Room
from player import Player
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east with a small alove to the west."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'nook':   Room("Small Nook", """You find the skeleton of an unlucky adventurer, turn back east before you meet the same end!"""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['foyer'].w_to = room['nook']
room['nook'].e_to = room['foyer']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

game_run = True
name = input("What is you name adventurer?:")
# Make a new player object that is currently in the 'outside' room.
player = Player(name, room["outside"])
print(f"Current Location: {player.current_room.name}, {player.current_room.description}")

directions = [ "n", "e", "s", "w" ]

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
while game_run:
    
    movement = input(f"{player.name} choose the direction you'd like to explore [N] [E] [S] [W] or [Q] to quit then [Enter]: ")

    if movement in directions :
        print(f"{player.name} is moving {movement}")
        player.move(movement)
       
    elif movement == "q":
        game_run = False

    else: 
        print("\n Invalid Input, try again")