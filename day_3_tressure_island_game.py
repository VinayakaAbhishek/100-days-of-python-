
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
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
direction=input("you're at a cross road with two directions to choose, what direction will you choose 'LEFT' or 'RIGHT' ")
direction=direction.lower()
if direction=="left":
    path=input('''you have arrived at a lake, there is an island in the middle of the lake.
    type "wait " if you wanna wait for the boat or type "swim" if you wanna die ''')
    path=path.lower()
else:
    print("you die looser, game is over ")

if path=="wait":

    choose_the_colour=input("You have safely reached the island, now there are three doors in front of you. One is red one is yellow and the last one is blue. choose which door you want to open")
    choose_the_colour=choose_the_colour.lower()

else:
    print("You die loose, The game is over")
if choose_the_colour=="red":
    print("you got destroyed by the red flames of hell")
elif choose_the_colour=="yellow":
    print("congratulations you found the bloody treasure, hope you're proud of winning a game designed for 2nd class students")
else:
    print("congratulations you are shark food now , you lost game over")