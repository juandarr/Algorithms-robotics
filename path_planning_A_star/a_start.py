'''
-----------
A* implementation for path planning in a 2D grid
Date: February 22/2019
Author: Juan David Rios

User Instructions:

 Modify the the search function so that it returns
 a shortest path as follows:
 
 [['v', ' ', ' ', ' ', ' ', ' ']
 ['v', ' ', ' ', ' ', ' ', ' ']
 ['v', ' ', ' ', ' ', ' ', ' ']
 ['v', ' ', ' ', '>', '>', 'v']
 ['>', '>', '>', '^', ' ', '*']]

 Where '>', '<', '^', and 'v' refer to right, left, 
 up, and down motions. Note that the 'v' should be 
 lowercase. '*' should mark the goal cell.

 You may assume that all test cases for this function
 will have a path from init to goal.
----------
'''

grid = [[0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0]]

heuristic = [[9, 8, 7, 6, 5, 4],
             [8, 7, 6, 5, 4, 3],
             [7, 6, 5, 4, 3, 2],
             [6, 5, 4, 3, 2, 1],
             [5, 4, 3, 2, 1, 0]]

# Initial position in grid
init = [0, 0]

# Goal position in grid
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

# Posible set of actions
delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right
# Actions in symbols
delta_name = ['^', '<', 'v', '>']

'''
A_start_search A* star function that defines the path followed by an agent 
in a grid from init position to goal position, with cost value per action and 
a heuristic matrix describing how far is each cell from the goal
@param grid The 2 dimension grid where the agent moves
@param heuristic Heuristic matrix
@param init Initial position
@param goal Goal position
@param cost The cost of each possible action 
@output path Return the path followed by the agent and the actions taken
'''
def A_star_search(grid,heuristic,init,goal,cost):
    # Expand grid to indicate which nodes are expanded in the algorithm
    expand = [[-1 for col in range(len(grid[0]))] for row in range(len(grid))]
    # Closed grid to define nodes as explored
    closed = [[0 for col in range(len(grid[0]))] for row in range(len(grid))]
    closed[init[0]][init[1]] = 1

    # Initial values
    x = init[0]
    y = init[1]
    g = 0
    f = g + heuristic[x][y]
    
    # Set of possible paths
    stateSet=[]
    state = [[' ' for col in range(len(grid[0]))] for row in range(len(grid))]
    stateSet.append(state)
    
    # List storing nodes to be expanded
    open = [[f, g, x, y]]

    # Expansion counter
    count = 0

    while True:
        # If there are no more nodes to expand, there is not solution
        if len(open) == 0:
            return 'fail'
        else:
            # Sort paths according to the f,g values of the respective end node
            stateSet = [s for _,s in sorted(zip(open,stateSet), reverse=True)]
            next_state = stateSet.pop()
            
            # Sort list of nodes to be expanded. Pop out the node withe the smallest f,g value
            open.sort(reverse=True)
            next = open.pop()

            # Node to be expanded
            x = next[2]
            y = next[3]
            g = next[1]
            expand[x][y] = count
            count += 1
            
            # If goal is reached, define asterisk in the goal node and return path
            if x == goal[0] and y == goal[1]:
                next_state[x][y] = '*'
                return next_state
            # Else expand node
            else:
                for i in range(len(delta)):
                    dir_state = [e[:] for e in next_state]
                    x2 = x + delta[i][0]
                    y2 = y + delta[i][1]
                    # If new node is between the x/y grid limits
                    if x2 >= 0 and x2 < len(grid) and y2 >=0 and y2 < len(grid[0]):
                        if closed[x2][y2] == 0 and grid[x2][y2] == 0:
                            g2 = g + cost
                            f = g2 + heuristic[x2][y2]
                            # Append node to the list of nodes to be expanded
                            open.append([f, g2, x2, y2])
                            # Close node
                            closed[x2][y2] = 1
                            # Store updated state
                            dir_state[x][y] = delta_name[i]
                            stateSet.append(dir_state)

states = A_star_search(grid, heuristic, init, goal, cost)

for i in states:
    print(i)
print(' ')

