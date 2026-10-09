print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to The Treasure secret Island.")
print("Your mission is to find the treasure.")
road= input('You are at a cross road. Where do you want to go?, type "Left" or "L" or "Right" or "R" \n').lower()
if road == "right" or road == "r":
    print("You've come across the lake.")
    lake = input('There is an island in the middle of the lake.Type "Wait" or "W" to wait for a boat. Type "Swim" or "S" to swim across. wait\n').lower()
    if lake == "wait" or lake == "w":
        print("Uh-oh, The Gang caught you, Game Over!")
    elif lake == "swim" or lake == "s":
        print("Good choice, You saved more time and you have arrived at the island unharmed.")
        choice = input('There is a house with 3 doors. One "Red" or "R", one "Yellow" or "Y" and one "Blue" or "B". Which colour do you choose?\n').lower()
        if choice == "yellow" or choice == "y":
            print("Well done You've find the treasure, You win!")
        elif choice == "red" or choice == "r":
            print("Uh-oh, this room is fired you've been died, Game Over! ")
        elif choice == "blue" or choice == "b":
            print("Uh-oh, You've entered the beast room. Game Over!")
        else:
            print("Please enter a valid choice.")
    else:
        print("Please enter a valid choice.")
elif road == "left" or road == "l":
    print("Uh-oh, You have fell down the hole, Game Over!")
else:
    print("Please enter a valid choice.")