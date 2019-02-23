# -----------
# User Instructions:
#
# Modify the the search function so that it returns
# a shortest path as follows:
# 
# [['v', ' ', ' ', ' ', ' ', ' ']
# ['v', ' ', ' ', ' ', ' ', ' ']
# ['v', ' ', ' ', ' ', ' ', ' ']
# ['v', ' ', ' ', '>', '>', 'v']
# ['>', '>', '>', '^', ' ', '*']]
#
# Where '>', '<', '^', and 'v' refer to right, left, 
# up, and down motions. Note that the 'v' should be 
# lowercase. '*' should mark the goal cell.
#
# You may assume that all test cases for this function
# will have a path from init to goal.
# ----------

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

#grid = [[0, 0],
#        [1, 0]]
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

def search(grid,heuristic,init,goal,cost):
    # ----------------------------------------
    # modify code below
    # ----------------------------------------
    expand = [[-1 for col in range(len(grid[0]))] for row in range(len(grid))]

    closed = [[0 for col in range(len(grid[0]))] for row in range(len(grid))]
    closed[init[0]][init[1]] = 1

    x = init[0]
    y = init[1]
    g = 0
    h = heuristic[x][y]
    
    stateSet=[]
    state = [[' ' for col in range(len(grid[0]))] for row in range(len(grid))]
    stateSet.append(state)
    
    open = [[h, g, x, y]]

    count = 0

    while True:
        if len(open) == 0:
            return 'fail',expand
        else:
            stateSet = [s for _,s in sorted(zip(open,stateSet), reverse=True)]
            next_state = stateSet.pop()
            
            open.sort(reverse=True)
            next = open.pop()

            x = next[2]
            y = next[3]
            g = next[1]
            print([x,y,g])
            expand[x][y] = count
            count += 1
            
            if x == goal[0] and y == goal[1]:
                next_state[x][y] = '*'
                return next_state, expand
            else:
                for i in range(len(delta)):
                    dir_state = [e[:] for e in next_state]
                    x2 = x + delta[i][0]
                    y2 = y + delta[i][1]
                    if x2 >= 0 and x2 < len(grid) and y2 >=0 and y2 < len(grid[0]):
                        if closed[x2][y2] == 0 and grid[x2][y2] == 0:
                            g2 = g + cost
                            h = g2 + heuristic[x2][y2]
                            dir_state[x][y] = delta_name[i]
                            stateSet.append(dir_state)
                            open.append([h, g2, x2, y2])
                            closed[x2][y2] = 1

states,exp= search(grid, heuristic, init, goal, cost)
for i in states:
    print(i)
print(' ')
for j in exp:
    print(j)
