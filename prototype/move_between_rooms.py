# A dictionary for the simplified dragon text game.
# The dictionary links a room to other rooms.
rooms = { 
'Gathering Room': {'South': 'Bedroom', 'North': 'Storage Room', 'West': 'Library'},
'Bedroom': {'North': 'Gathering Room'},
'Storage Room': {'South': 'Gathering Room'},
'Library': {'East': 'Gathering Room'},}

current_room = 'Gathering Room'
starting_room = current_room

while True:
    print (f"You are currently in {current_room}.")

player_input = input("Enter your move (or 'exit to quit'): ").strip().capitalize()

if player_input == "Exit": 
    print ("You are exiting the game. Thanks for playing!")

else:
    player_input = "North/South/East/West"

if player_input in rooms[current_room]:
    current_room = rooms[current_room][player_input]
    print ("You traveled {player_input}.")
else:
    print ("Wrong way! There is no room in that direction.")

print ("Invalid input. Please enter North, South, East, West, or Exit.")
