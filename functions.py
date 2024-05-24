#################################################
#================ Dice Roll ====================#
#################################################


import math
import random

#Twenty Sided Die
def d20():
    return random.randint(1, 20)


#Six Sided Die
def d6():
    return random.randint(1, 6)

#Handle the directions that the user would like to move        
def movement(pos_map, user_input):
    global user_pos
    new_pos = user_pos
    row, col = user_pos 
    if user_input == 'move up' and row > 0:
        new_pos = (row - 1, col)
    elif user_input == 'move down' and row < len(pos_map) - 1:
        new_pos = (row + 1, col)
    elif user_input == 'move left' and col > 0:
        new_pos = (row, col - 1)
    elif user_input == 'move right' and col < cols - 1:
        new_pos = (row, col + 1)
    else:
        print('You cannot move in that direction')
        
    pos_map[row][col], pos_map[new_pos[0]][new_pos[1]] = 'o', 'X'
    
    user_pos = new_pos
    return pos_map

rows, cols = (3, 5)
user_pos = (1, 2)

#Display updated map with player position
def display_map(pos_map):
    for row in pos_map:
        print(row)

#Create the map with position of player in the center
def create_map():
    map = [['o' for i in range(cols)] for j in range(rows)]
    map[user_pos[0]][user_pos[1]] = 'X'
    for row in map:
        print(row)
    return map
#pos_map = create_map()
