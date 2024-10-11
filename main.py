from TTTQlearning import TTTQlearning


def start_learning_TTT(startState, maxGames):
    """
    Starts the 4x4 Tic-tac-toe reinforcement learning process.
    """

    qlearn = TTTQlearning()
    state = startState
    games = 0
  
    while games < maxGames:  
            
        qlearn.addKey(state)
        # action = chooseAction(stateKey, table)

if __name__ == "__main__":

    MAX_GAMES = 100

    start_learning_TTT('_'*16 + 'X', MAX_GAMES)