from itertools import *
import string

f = open('/home/tom/Projects/ProjectEuler/files/triangle.txt', 'r')
file_contents=f.read()

lines=string.split(file_contents, "\n")

triangle=[string.split(i, " ") for i in lines]

max_sum=0

for i in range(16384):
    index=0
    max_path=""
    sum=int(triangle[0][0])
    # Generates a 14 digit long binary string to indicate left or right
    path=bin(i)[2::].zfill(14)

    for j in range(14):
        index+=int(path[j])
        sum+=int(triangle[j+1][index])
        
    if sum>max_sum:
        max_sum=sum
    
print max_sum
