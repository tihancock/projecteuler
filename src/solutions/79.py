"""
The strategy here is to create a set for each number composed of
numbers that precede it in the login key. Given sufficient login
attempts, the length of said set equates to the index of the number in
the login key.
"""

from string import split

key=['' for i in range(10)]
preceding_nums={}

lines=split(open('files/keylog.txt','r').read(),'\r\n')
attempts=[]
for l in lines:
    attempts.append([int(c) for c in l])

for a in attempts:
    if a[2] not in preceding_nums:
        preceding_nums[a[2]]=set()
    preceding_nums[a[2]].add(a[1])
    preceding_nums[a[2]].add(a[0])

    if a[1] not in preceding_nums:
        preceding_nums[a[1]]=set()
    preceding_nums[a[1]].add(a[0])

    if a[0] not in preceding_nums:
        preceding_nums[a[0]]=set()

for k in iter(preceding_nums):
    key[len(preceding_nums[k])]=k

print "".join([str(i) for i in key])


