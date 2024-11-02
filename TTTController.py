from abc import ABC, abstractmethod


class TTTController:

    def __init__(self):
        """
        This class deals with all complexities of tic-tac-toe game.
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


    @abstractmethod
    def is_game_over(self, state):
        """
        Checks if the game is over. X wins -> +1, O wins -> -1

        INPUTS:
            * state (str): current board state.
        OUTPUTS:
            * boolean: True if game has ended
        """
        pass


    @abstractmethod
    def print_grid(self, state):
        """
        Draws the 4x4 board.

        INPUTS:
            * state (str): current board state.
        """
        pass