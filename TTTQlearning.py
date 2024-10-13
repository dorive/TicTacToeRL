import random
from TTTController import TTTController

class TTTQlearning:

    def __init__(self, ttt_controller:TTTController):
        self.gameController = ttt_controller
        self.statesScores = {}
        self.statesNext = {}
        self.discount = 0.1
        self.learningRate = 0.1


    def addKey(self, state):
        """
        Adds a state into the states dictionary.

        INPUTS:
            - state (str): state in standard format
        """

        # Player at state
        player = state[-1]

        if state not in self.statesNext:
            # Get next states
            next_states = self.gameController.get_next_states(state)

            # Fill values for next states
            self.statesNext[state] = []

            for st in next_states:
                self.statesNext[state].append(st)

                if st not in self.statesScores:
                    game_over, score = self.gameController.is_game_over(state)
                    if game_over:
                        self.statesScores[st] = score
                    else:
                        self.statesScores[st] = random.uniform(-0.15, 0.15)

            if player == 'X':
                self.statesScores[state] = self.lowestQvalue(state)
            else:
                self.statesScores[state] = self.highestQvalue(state)
            

    def chooseActionNaive(self, state):
        """
        Action will be chosen in a naively. 
        If random number > 0.5 then best action will be taken, 
        if not random action will performed.

        INPUTS:
            * state (str): state in standard format
        OUTPUTS:
            * (str) it will return the selected state.
            * (float) it will return the reward.
        """

        rdn = random.uniform(0, 1.0)
        tuples = [(st, self.statesScores[st]) for st in self.statesNext[state]]

        if rdn >= 0.5:
            max_tuple = max(tuples, key=lambda x: x[1])
            return max_tuple[0], max_tuple[1]
        else:
            rnd_tuple = random.choice(tuples)
            return rnd_tuple[0], rnd_tuple[1]


    def lowestQvalue(self, state):
        """
        Returns the lowest reward action from given state.

        INPUTS:
            * state (str): state in standard format
        OUTPUTS:
            * (float) it will return the lowest reward.
        """

        return min([self.statesScores[st] for st in self.statesNext[state]])
    

    def highestQvalue(self, state):
        """
        Returns the highest reward action from given state.

        INPUTS:
            * state (str): state in standard format
        OUTPUTS:
            * (float) it will return the lowest reward.
        """

        return max([self.statesScores[st] for st in self.statesNext[state]])
    

    def updateQvalues(self, state, next_state, reward):
        """
        Update the Q value of the state.

        INPUTS:
            * state (str): state in standard format
            * next_state (str): chosen next state, in standard format
            * reward (float): obtained reward
        """

        # Player at state
        player = state[-1]

        if self.gameController.is_game_over(next_state)[0]:
            expected = reward
        else:
            if player == 'X':
                expected = reward + (self.discount * self.lowestQvalue(next_state))
            else:
                expected = reward + (self.discount * self.highestQvalue(next_state))
        
        change = self.learningRate * (expected - self.statesScores[next_state])

        if self.gameController.is_game_over(next_state)[0] and change != 0.0:
            import pdb
            pdb.set_trace()

        self.statesScores[next_state] += change

