print('''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

choice = input("Choose direction to move (left or right): ").lower()
if choice != 'left':
    print('Ooops, you died :)')
    quit(0)

print("You see a lake with an island in the middle of it.")
choice = input("What are you going to do (swim or wait): ").lower()
if choice != 'wait':
    print('Ooops, you were eaten by salmon :)')
    quit(0)

print("The boat has come and moved you to the island.")
print("Now you see a house with three doors - red, blue and yellow.")
choice = input("Which one do you choose (red, blue or yellow): ").lower()
if choice == "red":
    print("You step into fire and die :)")
elif choice == "blue":
    print("Those beasts were very hungry, thanks for cooperation. Yes, you died :)")
elif choice == "yellow":
    print("Lucky bastard, you found a princess and spent very good time ;)")
else:
    print("Bad choice, you died :)")
