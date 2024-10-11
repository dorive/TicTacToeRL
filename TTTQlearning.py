import random
from TTTController import TTTController

class TTTQlearning:

    def __init__(self):
        self.gameController = TTTController()
        self.stateDict = {}

    def addKey(self, state):
        """
        Adds a state into the states dictionary.

        INPUTS:
            - state (str): state in standard format
        """

        if state not in self.stateDict:
            # Get next states
            next_states = self.gameController.get_next_states()

            # Fill values for next states
            self.stateDict[state] = [self.stateDict[st] if (st in self.stateDict) else random.uniform(-0.15, 0.15) for st in next_states]

    def chooseActionNaive(self, state):
        pass