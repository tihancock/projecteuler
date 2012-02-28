import string
from copy import deepcopy

def findMaxSum(tree, level, pos):
    if level==len(tree)-1:
        return tree[level][pos]
    else:
        return tree[level][pos]+max(tree[level+1][pos],
                                    tree[level+1][pos+1])

f = open('files/triangle.txt', 'r')

lines=string.split(f.read(), "\n")

triangle=[[int(j) for j in string.split(i, " ")] for i in lines]

# Copy the triangle before we start calculating the max branches
maxSums=deepcopy(triangle)

# Traverse up the tree, choosing the maximum branch each time
for i in range(len(maxSums))[::-1]:
    for j in range(len(maxSums[i])):
        maxSums[i][j]=findMaxSum(maxSums,i,j)

""" The top element of the tree is now equal to the sum of the nodes
    of the max branch"""
print maxSums[0][0]
