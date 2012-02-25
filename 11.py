import string

f = open('/home/tom/Projects/ProjectEuler/files/20_20_grid.txt', 'r')
file_contents=f.read()
largest_seq=0

lines=string.split(file_contents, "\n")
matrix=[string.split(i," ") for i in lines]
number_matrix=[map(lambda x: int(x), matrix[i]) for i in range(20)]

for i in range(4, 20):
    for j in range(4, 20):
        across=number_matrix[i][j]*number_matrix[i][j-1]*number_matrix[i][j-2]*number_matrix[i][j-3]
        down =number_matrix[i][j]*number_matrix[i-1][j]*number_matrix[i-2][j]*number_matrix[i-3][j]
        diag_l =number_matrix[i][j]*number_matrix[i-1][j-1]*number_matrix[i-2][j-2]*number_matrix[i-3][j-3]
        diag_r =number_matrix[i][j-3]*number_matrix[i-1][j-2]*number_matrix[i-2][j-1]*number_matrix[i-3][j]
        if (across > largest_seq):
            largest_seq=across
        if (down > largest_seq):
            largest_seq=down
        if (diag_l > largest_seq):
            largest_seq=diag_l
        if (diag_r > largest_seq):
            largest_seq=diag_r
            
print largest_seq
