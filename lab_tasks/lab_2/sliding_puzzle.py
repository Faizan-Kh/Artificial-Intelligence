# Define the goal state and start state
goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)
start = (8, 2, 0, 4, 7, 6, 3, 5, 1)

# Define functions to print states and puzzle
def printstate(state):
    """
    Prints states in a 3x3 tabular form
    """
    print(state[0:3])
    print(state[3:6])
    print(state[6:9])

def printpuzzle(state):
    """
    Prints the puzzle state in a better looking form
    """
    print('_______\n|{}|{}|{}|\n|{}|{}|{}|\n|{}|{}|{}|\n_______'.format(state[
0],
state[1],
state[2],
state[3],
state[4],
state[5],
state[6],
state[7],
state[8],
))

# Define the transition model function
def result(statein, action):
    """
    Returns the state produced as a result of performing 'action'
    on the given state 'statein'
    """
    stateout = list(statein)  # make a local copy of statein
    if action == 'Up':
        idx = statein.index(0)
        if idx not in [0, 1, 2]:  # check if the blank position is not in the top row
            stateout[idx], stateout[idx - 3] = stateout[idx - 3], stateout[idx]  # swap with the upper tile
    elif action == 'Down':
        idx = statein.index(0)
        if idx not in [6, 7, 8]:  # check if the blank position is not in the bottom row
            stateout[idx], stateout[idx + 3] = stateout[idx + 3], stateout[idx]  # swap with the lower tile
    elif action == 'Left':
        idx = statein.index(0)
        if idx not in [0, 3, 6]:  # check if the blank position is not in the leftmost column
            stateout[idx], stateout[idx - 1] = stateout[idx - 1], stateout[idx]  # swap with the left tile
    elif action == 'Right':
        idx = statein.index(0)
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

# Define a function to solve the puzzle automatically given a starting sequence
def solve_sliding_puzzle(start_state):
    frontier = [(start_state, [])]  # Queue of states and their path to the current state
    explored = set()  # Set of explored states
    while frontier:
        state, path = frontier.pop(0)  # Get the current state and its path
        if state == goal:
            return path
        explored.add(state)
        for action in ['Up', 'Down', 'Left', 'Right']:
            new_state = result(state, action)
            if new_state not in explored:
                frontier.append((new_state, path + [action]))
                explored.add(new_state)
    return None  # No solution found

# Additional Task: Function to solve and display each step to solve the puzzle
def solve_and_display(start_state):
    solution = solve_sliding_puzzle(start_state)
    if solution:
        print("Solution steps:")
        current_state = start_state
        for action in solution:
            current_state = result(current_state, action)
            printpuzzle(current_state)
    else:
        print("No solution found.")

# Play the sliding puzzle game
play_sliding_puzzle(start)

# Additional Task: Solve and display the puzzle given a starting sequence
starting_sequence = tuple(map(int, input("Enter starting sequence (comma-separated): ").split(',')))
solve_and_display(starting_sequence)
