# Define the goal state and start state
goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)
start = (8, 2, 0, 4, 7, 6, 3, 5, 1)

# Define functions to print states and puzzle
def printpuzzle(state):
    """
    Prints the puzzle state in a better-looking form
    """
    print('_______\n|{}|{}|{}|\n|{}|{}|{}|\n|{}|{}|{}|\n_______'.format(state[0], state[1], state[2],
                                                                          state[3], state[4], state[5],
                                                                          state[6], state[7], state[8]))

# Define the transition model function
def result(statein, action):
    """
    Returns the state produced as a result of performing 'action'
    on the given state 'statein'
    """
    stateout = list(statein)  # make a local copy of statein
    idx = statein.index(0)  # find the index of the blank position
    if action == 'Up':
        if idx not in [0, 1, 2]:  # check if the blank position is not in the top row
            stateout[idx], stateout[idx - 3] = stateout[idx - 3], stateout[idx]  # swap with the upper tile
    elif action == 'Down':
        if idx not in [6, 7, 8]:  # check if the blank position is not in the bottom row
            stateout[idx], stateout[idx + 3] = stateout[idx + 3], stateout[idx]  # swap with the lower tile
    elif action == 'Left':
        if idx not in [0, 3, 6]:  # check if the blank position is not in the leftmost column
            stateout[idx], stateout[idx - 1] = stateout[idx - 1], stateout[idx]  # swap with the left tile
    elif action == 'Right':
        if idx not in [2, 5, 8]:  # check if the blank position is not in the rightmost column
            stateout[idx], stateout[idx + 1] = stateout[idx + 1], stateout[idx]  # swap with the right tile
    return tuple(stateout)

# Define the main function to play the game
def play_sliding_puzzle(start_state):
    current_state = start_state
    while current_state != goal:
        printpuzzle(current_state)
        action = input("Enter action (Up/Down/Left/Right): ")
        if action in ['Up', 'Down', 'Left', 'Right']:
            current_state = result(current_state, action)
        else:
            print("Invalid action! Please enter Up/Down/Left/Right.")
    print("Congratulations! You solved the puzzle.")

# Play the sliding puzzle game
play_sliding_puzzle(start)
