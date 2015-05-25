#!usr/bin/python
from random import choice

cave_numbers = range(1,21)
wumpus_location = choice(cave_numbers)
wumpus_friend_location = choice(cave_numbers)
player_location = choice(cave_numbers)
while (player_location == wumpus_location or 
       player_location == wumpus_friend_location):
       player_location = choice(cave_numbers)

print "Welcome to Hunt the Wumpus!"
print "You can see", len(cave_numbers), "caves"
print "To play, just type the number"
print "of the cave you wish to enter next"


while True:
    print "you are in cave", player_location
    print "wumpus is in cave", wumpus_location
    print "wumpus friend is in cave", wumpus_friend_location
    if (player_location == wumpus_location - 1 or 
        player_location == wumpus_location + 1):
	print "I smell a wumpus"
	break

    if (player_location == wumpus_friend_location -1 or
        player_location == wumpus_friend_location +1):
        print "I smell a wumpus friend!"
	break

    else:   
        print "Which cave next?"
        player_input = raw_input(">")
        if (not player_input.isdigit() or
            int(player_input) not in cave_numbers):
            print player_input, "Is not a cave!"

        else:
            player_location = int(player_input)
            if player_location == wumpus_location:
                print "Aargh! You got eaten by a wumpus!"
                break
            if player_location == wumpus_friend_location:
                print "Argh! You got eaten by the wumpus friend!"
                break
