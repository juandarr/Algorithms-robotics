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
Z = 'red'
pHit = 0.6
pMiss = 0.2

def sense(p, Z):
    q=[]
    for i in range(len(p)):
        hit = (Z == world[i])
        q.append(p[i] * (hit * pHit + (1-hit) * pMiss))
    total = float(sum(q))
    for i in range(len(q)):
        q[i] /= total
    return q
    
print(sense(p,Z))