import logging
import json
from TTTQlearning import TTTQlearning
from TTTController import TTTController

# Set up basic configuration for logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')


def start_learning_TTT(startState, maxGames):
    """
    Starts the 4x4 Tic-Tac-Toe reinforcement learning process.
    """

    game_controller = TTTController()
    qlearn = TTTQlearning(game_controller)
    state = startState
    games = 0
  
    while games < maxGames:  

        print(state)

        # Add state if new
        qlearn.addKey(state)

        # Choose an action naively
        next_state, _ = qlearn.chooseActionNaive(state)
        reward = game_controller.get_reward(next_state)
        qlearn.addKey(next_state)

        # Update the Q value for the state
        qlearn.updateQvalues(state, next_state, reward)

        # If game has not ended then keep playing
        if game_controller.is_game_over(next_state)[0]:
            logging.info(f'Game {games+1} from {maxGames} is over.')
            state = '_'*16 + 'X'
            games += 1
        else:
            state = next_state

    return qlearn.statesScores


if __name__ == "__main__":

    MAX_GAMES = 100000

    Q = start_learning_TTT('_'*16 + 'X', MAX_GAMES)

    # Save dictionary to a JSON file
    with open(f"Q_{MAX_GAMES}iters_4x4.json", "w") as json_file:
        json.dump(Q, json_file)