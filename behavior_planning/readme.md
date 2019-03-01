# Behavior planning algorithm

## Description  

This code implements a behavior planner using a set of cost functions to define the transition function in a finite state machine setting. The goal is given a set of possible next state define the best possible trajectory followed by a car for highway driving. The planner will use prediction data to set the state of the vehicle to one of 5 values and generate a corresponding vehicle trajectory: 

- `KL`: keep lane
- `LCL` \ `LCR`: Lane Change Left \ Lane Change Right
- `PLCL` \ `PLCR`: Prepare Lane Change Left \ Prepare Lane Change Right

The main logic uses a given map, set of predictions, locations, current state of the agent and a speed limit to define the best behavior to follow that will result in a desired trajectory with minimal cost.

## Instructions

The main program can be built and ran by calling the following scripts from the project top directory:

- ./build.sh
- ./run.sh
 
Any executables can be removed with the following script:

 - ./clean.sh