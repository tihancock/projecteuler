from itertools import *
import string

f = open('files/triangle_18.txt', 'r')
file_contents=f.read()

lines=string.split(file_contents, "\n")

triangle=[string.split(i, " ") for i in lines]

max_sum=0

# Generate a 14 character binary string representing each path
for i in range(16384):
    index=0
    max_path=""
    sum=int(triangle[0][0])
    # 0 indicates left, 1 right
    path=bin(i)[2::].zfill(14)

    for j in range(14):
        index+=int(path[j])
        sum+=int(triangle[j+1][index])
        
    if sum>max_sum:
        max_sum=sum
    
print max_sum
