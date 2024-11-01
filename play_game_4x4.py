import json
from TTTController import TTTController

# Load dictionary from a JSON file
with open("Q_100000iters_4x4.json", "r") as json_file:
    Q = json.load(json_file)

# Load game controller
game_controller = TTTController()

# Prompt user until a valid input ('X' or 'O') is provided
while True:
    choice = input("What side do you want to play? ('X' or 'O'): ").upper()
    if choice in ['X', 'O']:
        print(f"You chose: {choice}")
        break
    else:
        print("Invalid input. Please enter only 'X' or 'O'.")

# Start game
game_state = '_'*16 + 'X'
side_turn  = game_state[-1]

while not game_controller.is_game_over(game_state)[0]:

    if choice == side_turn: # Human plays

        game_controller.print_grid(game_state[:-1])

        while True:

            coordinates = input("Enter your move coordinates (e.g. 1,2): ").upper()
            # Check if input is in the correct format
            try:
                row, col = map(int, coordinates.split(','))
                row_index = row - 1
                col_index = col - 1
                index = row_index * 4 + col_index
                if game_state[index] == '_':
                    break  # Exit loop if input is valid
            except ValueError:
                print("Invalid format. Please enter coordinates as two numbers separated by a comma (e.g., 1,2).")

        # Change turns
        side_turn = 'O' if side_turn == 'X' else 'X'

        # Update board
        game_state = game_state[:index] + 'X' + game_state[index + 1:-1] + side_turn
        game_controller.print_grid(game_state[:-1])


    else: # Machine plays
        print('Machine plays...')

        next_states = game_controller.get_next_states(game_state)
        game_state = min(next_states, key=lambda k: Q[k])
        
        # Change turns
        side_turn = 'O' if side_turn == 'X' else 'X'
        game_state = game_state[:-1] + side_turn
        
_, result = game_controller.is_game_over(game_state)

# Print final board
print('-'*16)
print('Final game state')
game_controller.print_grid(game_state[:-1])
print('-'*16)

if ((result == 1) and (choice == 'X')) or ((result == -1) and (choice == 'O')):
    print('You won!')
elif result == 0:
    print(r"It's a draw")
else:
    print('You lost...')