'''
 ----------
Dynamic programming implementation for path planning in a 2D grid
Date: February 22/2019
Author: Juan David Rios

 User Instructions:
 
 Implement the function optimum_policy below.

 You are given a car in grid with initial state
 init. Your task is to compute and return the car's 
 optimal path to the position specified in goal; 
 the costs for each motion are as defined in cost.

 There are four motion directions: up, left, down, and right.
 Increasing the index in this array corresponds to making a
 a left turn, and decreasing the index corresponds to making a 
 right turn.
'''

forward = [[-1,  0], # go up
           [ 0, -1], # go left
           [ 1,  0], # go down
           [ 0,  1]] # go right
forward_name = ['up', 'left', 'down', 'right']

# action has 3 values: right turn, no turn, left turn
action = [-1, 0, 1]
action_name = ['R', '#', 'L']

# EXAMPLE INPUTS:
# grid format:
#     0 = navigable space
#     1 = unnavigable space 

grid = [[1, 1, 0, 0, 0, 0, 0, 0],
        [1, 1, 0, 1, 1, 1, 0 ,1],
        [0, 1, 0, 1, 1, 0, 0, 0],
        [0, 1, 0, 1, 1, 1, 1, 0],
        [0, 0, 0, 1, 0, 0, 0, 0]]
        
init = [4, 4, 3] # given in the form [row,col,direction]
                 # direction = 0: up
                 #             1: left
                 #             2: down
                 #             3: right
                
goal = [2, 0] # given in the form [row,col]

cost = [2, 1, 20] # cost has 3 values, corresponding to making 
                  # a right turn, no turn, and a left turn

# EXAMPLE OUTPUT:
# calling optimum_policy2D with the given parameters should return 
# [[' ', ' ', 'L', '#', '#', '#', 'L', ' ']
# [' ', ' ', '#', ' ', ' ', ' ', '#', ' ']
# ['*', ' ', '#', ' ', ' ', ' ', 'R', 'L']
# ['#', ' ', '#', ' ', ' ', ' ', ' ', '#']
# ['R', '#', 'R', ' ', '#', '#', '#', 'L']]
# ----------

# ----------------------------------------
# modify code below
# ----------------------------------------

def optimum_policy(grid,init,goal,cost):
    # Value set for all possible orientations
    values = [[[999 for row in range(len(grid[0]))] for col in range(len(grid))],
             [[999 for row in range(len(grid[0]))] for col in range(len(grid))],
             [[999 for row in range(len(grid[0]))] for col in range(len(grid))],
             [[999 for row in range(len(grid[0]))] for col in range(len(grid))]]
    
    # Policy grid, indicates the set of actions followed by the agent
    policy = [[' ' for row in range(len(grid[0]))] for col in range(len(grid))]
    policy[goal[0]][goal[1]] = '*'
    change = True
    
    while change:
        change = False
        
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                # For each possible orientation 
                for z in range(len(forward)):
                    # if x,y position is the goal, initialize the value in the values set
                    if goal[0] == x and goal[1] == y:
                        if values[z][x][y] > 0:
                            values[z][x][y] = 0
                            change = True
                    # Else if the location is free, apply an action from the set of actions
                    elif grid[x][y] == 0:
                        
                        for a in range(len(action)):
                            # New orientation given the action 
                            next_z = (z+action[a])%4
                            # New x coordinate after action
                            x2 = x + forward[next_z][0]
                            # New y coordinate after action
                            y2 = y + forward[next_z][1]
                            
                            if x2 >= 0 and x2 < len(grid) and y2 >= 0 and y2 < len(grid[0]) and grid[x2][y2] == 0:
                                if grid[x2][y2]==0:
                                    
                                    v2 = values[next_z][x2][y2] + cost[a]
                                    if v2 < values[z][x][y]:
                                        change = True
                                        values[z][x][y] = v2
    '''
    This section of the code starts from the initial node and defined the optimal policy 
    given the costs defined in the set of values for all orientations
    '''                                 
    x = init[0]
    y = init[1]
    z = init[2]
    
    while [x,y]!=goal:
        val = 999
        best_action = None
        next_state = None

        for a in range(len(action)):
            # For a given action calculate the next state
            z2 = (z+action[a])%4
            x2 = x + forward[z2][0]
            y2 = y + forward[z2][1]

            # If new state is within limits
            if x2 >= 0 and x2 < len(grid) and y2 >= 0 and y2 < len(grid[0]) and grid[x2][y2] == 0:
                # Take the smallest value representing the next state, save the action producing
                # that next state too
                if val > values[z][x2][y2]:
                    val = values[z][x2][y2]
                    next_state = [x2,y2,z2]
                    best_action = action_name[a] 
        # Store optimal next action in x,y policy position
        policy[x][y] = best_action
        # If there is not next state, no solution found
        if next_state==None:
            return 'fail'
        x,y,z = next_state
    return policy

policy = optimum_policy(grid, init, goal, cost)

for i in policy:
    print(i)
