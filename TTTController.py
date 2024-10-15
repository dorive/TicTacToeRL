class TTTController:

    def __init__(self):
        """
        This class deals with all complexities of 4x4 tic-tac-toe game.
        """
        pass


    def get_next_states(self, state):
        """
        Returns the possible next state from current state.

        INPUTS:
            * state (str): current board state.
        OUTPUTS:
            * list of states.
        """

        # Get player turn
        player = state[-1]
        state = state[:-1]

        # Player at next turn
        next_player = 'X' if player == 'O' else 'O'

        # List to store all possible next states
        next_states = []
        
        # Iterate over the board and generate new states by placing the player's symbol in empty positions
        for i, cell in enumerate(state):
            if cell == '_':
                # Create a new state by replacing the empty cell with the current player's symbol
                new_state = state[:i] + player + state[i+1:] + next_player
                next_states.append(new_state)
        
        return next_states


    def is_game_over(self, state):
        """
        Checks if the game is over. X wins -> +1, O wins -> -1

        INPUTS:
            * state (str): current board state.
        OUTPUTS:
            * boolean: True if game has ended
        """

        # Remove player turn
        state = state[:-1]

        # Check that the state is correct
        if len(state) != 16:
            raise ValueError('Board state length is not correct!')

        # CASE 1: all corners are taken by the same player
        if (state[0] != '_') and (state[0] == state[3] == state[12] == state[15]):
            if state[0] == 'X':
                return True, 1
            else:
                return True, -1

        # Convert board string to a 4x4 list
        state = [state[i:i+4] for i in range(0, 16, 4)]

        # CASE 2: Four in a row (vertical, horizontal or diagonal)
        for row in state: # Check rows
            if (row[0] != '_') and (row.count(row[0]) == 4):
                if row[0] == 'X':
                    return True, 1
                else:
                    return True, -1
            
        for col in range(4): # Check columns
            column = [state[row][col] for row in range(4)]
            if (column[0] != '_') and (column.count(column[0]) == 4):
                if column[0] == 'X':
                    return True, 1
                else:
                    return True, -1

        # Check diagonals
        diagonal1 = [state[i][i] for i in range(4)]
        diagonal2 = [state[i][3-i] for i in range(4)]
        
        if diagonal1[0] != '_' and diagonal1.count(diagonal1[0]) == 4:
            if diagonal1[0] == 'X':
                return True, 1
            else:
                return True, -1
        if diagonal2[0] != '_' and diagonal2.count(diagonal2[0]) == 4:
            if diagonal2[0] == 'X':
                return True, 1
            else:
                return True, -1

        # CASE 3: Four in a square (2x2)
        for i in range(3):
            for j in range(3):
                square = [state[i][j], state[i][j+1], state[i+1][j], state[i+1][j+1]]
                if square[0] != '_' and square.count(square[0]) == 4:
                    if square[0] == 'X':
                        return True, 1
                    else:
                        return True, -1
                    
        # CASE 4: Draw
        if '_' not in ''.join(state):
            return True, 0
    
        return False, 0
    

    def get_reward(self, state):
        """
        Returns the reward for tic tac toe game.

        INPUTS:
            * state (str): current board state.
        OUTPUTS:
            * reward (float)
        """

        _, reward = self.is_game_over(state)
        return reward
    

    def print_grid(self, state):
        """
        Draws the 4x4 board.

        INPUTS:
            * state (str): current board state.
        """

        for i in range(0, len(state), 4):
            print(state[i:i+4])