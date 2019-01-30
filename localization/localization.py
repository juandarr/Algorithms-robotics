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

p=[0.2, 0.2, 0.2, 0.2, 0.2]
world=['green', 'red', 'red', 'green', 'green']
measurements = ['red', 'green']
motions = [1,1]
pHit = 0.6
pMiss = 0.2

pExact = 0.8
pOvershoot = 0.1
pUndershoot = 0.1
prob = [pUndershot, pExact, pOvershoot]

def sense(p, Z):
    """
    Changes the probability distribution based on the observation Z
    and the measure probability pHit, pMiss
    """
    q=[]
    for i in range(len(p)):
        hit = (Z == world[i])
        q.append(p[i] * (hit * pHit + (1-hit) * pMiss))
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
        q.append(p[i-U+1]*prob[0]+p[i-U]*prob[1]+p[i-U-1]*prob[2])
    return q

print(sense(p,Z))