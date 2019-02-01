"""
Purpose: basic localization algorithm implementation in python

Detailed description: Given the list motions=[1,1] which means the robot 
moves right and then right again, compute the posterior 
distribution if the robot first senses red, then moves 
right one, then senses green, then moves right again, 
starting with a uniform prior distribution.

Date: 01/29/2019

Author: Juan David Rios
"""

#Uniform probability distribution
p=[0.2, 0.2, 0.2, 0.2, 0.2]
#Information of the world
world=['green', 'red', 'red', 'green', 'green']
#Observation at time 0 and 1
measurements = ['red', 'red']
#Moves at time 0 and 1
motions = [1,1]

#Probability factor update when the observation coincides with the world state
pHit = 0.6
#Probability factor update when the observation doesn't coincide with the world state
pMiss = 0.2

#Probability factor of moving to the correct position
pExact = 0.8
#Probability factor of moving U steps after the correct position
pOvershoot = 0.1
#Probability factor of moving U steps before the correct position
pUndershoot = 0.1


def sense(p, Z):
    """
    Changes the probability distribution based on the observation Z
    and the measure probability pHit, pMiss
    """
    q = [p[i]*pHit if world[i]==Z else p[i]*pMiss for i in range(len(p))]
    total = float(sum(q))
    for i in range(len(q)):
        q[i] /= total
    return q

def move(p, U):
    """
    Moves the agent and updates the probability distribution with a convolution
    """
    q = []
    for i in range(len(p)):
        q.append(p[i-U+1]*pUndershoot + p[i-U]*pExact + p[i-U-1]*pOvershoot)
    return q

#Test localization algorithm with the repetition of the loop sense-motion in a sequence of data points
for i in range(len(measurements)):
    p =  sense(p, measurements[i])
    p = move(p, motions[i])

#Probability distribution after sense with measurements[0], move with motions[0], 
#sense with measurements[1] and move with motions[1]
print(p)