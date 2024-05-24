import main
import functions

print('Welcome Brave Player! You will be teleported to a dungeon and be asked to find and defeat the boss!')
print('Throughout the game, you can input move + direction(up, down, left, or right), attack, or heal')
print('If you forget the commands, write "help". If you want to quit, type "quit"')
print('Here is the starting map, you start in the middle where the X is:')
pos_map = functions.create_map()
game_input = 'start'
while game_input != 'quit':
    user_input = input('What would you like to do? ')
    game_input = user_input.lower()
    if game_input == 'help':
        print('Commands: move + direction, attack, heal, map')
    elif game_input == 'map':
        functions.display_map(pos_map)
    elif game_input in ['move up', 'move down', 'move left', 'move right']:
        pos_map = functions.movement(pos_map, game_input)
        print(f'You {game_input} a room on the map')
    elif game_input == 'quit':
        print('Thanks for Playing!')
    else: 
        print('I am not familiar with that command. Please check your spelling and try again.')
        print('If you need help with the commands, just type "help" and all acceptable commands will pop up!')
  