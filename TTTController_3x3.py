from TTTController import TTTController


class TTTController_3x3(TTTController):

    def __init__(self):
        """
        This class deals with all complexities of 3x3 tic-tac-toe game.
        """
        self.board_len = 3


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
        if len(state) != self.board_len**2:
            raise ValueError('Board state length is not correct!')

        # Convert board string to a 3x3 list
        state = [state[i:i+self.board_len] for i in range(0, self.board_len**2, self.board_len)]

        # CASE 1: Three in a row (vertical, horizontal or diagonal)
        for row in state: # Check rows
            if (row[0] != '_') and (row.count(row[0]) == self.board_len):
                if row[0] == 'X':
                    return True, 1
                else:
                    return True, -1
            
        for col in range(self.board_len): # Check columns
            column = [state[row][col] for row in range(self.board_len)]
            if (column[0] != '_') and (column.count(column[0]) == self.board_len):
                if column[0] == 'X':
                    return True, 1
                else:
                    return True, -1

        # Check diagonals
        diagonal1 = [state[i][i] for i in range(self.board_len)]
        diagonal2 = [state[i][self.board_len-1-i] for i in range(self.board_len)]
        
        if diagonal1[0] != '_' and diagonal1.count(diagonal1[0]) == self.board_len:
            if diagonal1[0] == 'X':
                return True, 1
            else:
                return True, -1
        if diagonal2[0] != '_' and diagonal2.count(diagonal2[0]) == self.board_len:
            if diagonal2[0] == 'X':
                return True, 1
            else:
                return True, -1

        # CASE 2: Draw
        if '_' not in ''.join(state):
            return True, 0
    
        return False, 0
    

    def print_grid(self, state):
        """
        Draws the 3x3 board.

        INPUTS:
            * state (str): current board state.
        """

        for i in range(0, len(state), self.board_len):
            print(state[i:i+self.board_len])