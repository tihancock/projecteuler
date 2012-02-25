import string
import re

f=open('/home/tom/Projects/ProjectEuler/files/names.txt','r')
file_contents=f.read()

sorted_names=sorted(string.split(re.sub("\"", "", file_contents), ","))
total_name_score=0

for i in range(len(sorted_names)):
    name_score=0
    for j in range(0, len(sorted_names[i])):
        name_score+=string.uppercase.index(sorted_names[i][j])+1
    total_name_score+=name_score*(i+1)

print total_name_score
