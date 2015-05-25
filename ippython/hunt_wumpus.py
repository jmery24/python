#!usr/bin/python
from random import choice

# new section 1
cave_numbers = range(0,20)
caves = []
for i in cave_numbers:
    caves.append([])

for i in cave_numbers:
    for j in range(3):
        passage_to = choice(cave_numbers)
        caves[i].append(passage_to)
print caves

wumpus_location = choice(cave_numbers)
player_location = choice(cave_numbers)
while player_location == wumpus_location:
    player_location = choice(cave_numbers)

print "Welcome to Hunt the Wumpus!"
print "You can see", len(cave_numbers), "caves"
print "To play, just type the number"
print "of the cave you wish to enter next"

# new section 4
while True:
    print "you are in cave", player_location
    print "wumpus is in cave", wumpus_location
    print "From here, you can see caves:", caves[player_location]
    if wumpus_location in caves[player_location]:
       print "I smell a wumpus"
       break

# old section 4
#    print "you are in cave", player_location
#    print "wumpus is in cave", wumpus_location
#    if (player_location == wumpus_location - 1 or
#        player_location == wumpus_location + 1):
#        print "I smell a wumpus!"
#        break

# new section 5
    else:
        print "Which cave next?"
        player_input = raw_input(">")
        if (not player_input.isdigit() or
            int(player_input) not in caves[player_location]):
            print player_input + "?"
            print "That's not a direction that I can see!"
            continue

# old section 5
#        print "Which cave next?"
#        player_input = raw_input(">")
#        if (not player_input.isdigit() or
#            int(player_input) not in cave_numbers):
#            print player_input, "Is not a cave!"

        else:
            player_location = int(player_input)
            if player_location == wumpus_location:
                print "Aargh! You got eaten by a wumpus!"
                break
