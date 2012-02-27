import re

f = open('files/words.txt','r')

words=re.sub('"','',f.read()).split(',')

max_triangle_num = (len(max(words, key=len))+1)*26 # letters of the alphabet

# generate triangle nums array
triangle_nums=[]
n = 1
while n*(n+1)/2 <= max_triangle_num:
    triangle_nums.append(n*(n+1)/2)
    n+=1

count=0
for w in words:
    if sum([ord(w[i])-64 for i in range(len(w))]) in triangle_nums:
        count+=1

print count
