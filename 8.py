import re

f = open('files/1000_digit_number.txt', 'r')
file_contents=f.read()

numbers = re.sub("[^0-9]","",file_contents)

largest_seq=0
for i in range (4, 1000):
    seq=int(numbers[i])*int(numbers[i-1])*int(numbers[i-2])*int(numbers[i-3])*int(numbers[i-4])
    if (seq > largest_seq):
        largest_seq=seq
        
print largest_seq
