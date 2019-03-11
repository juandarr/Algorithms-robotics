# Hybrid A* implementation in C++

This program implements the continuous search space variation of the A* algorithm used in Path planning to find drivable trajectories to follow in a restricted situation, such as a parking lot. Hybrid A star uses an optimistic heuristic function to guide grid cell expansion. Two advantages lost in the transition from discrete (the original A* method) to continous is that now there is no guarantee of **completeness** (that there is a solution) or **optimality** (that the solution, if found will be optimal).

