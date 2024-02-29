from random import randint
from time import time 


a = [[randint(1, 10) for k in range(1000)] for i in range(1000)]       # THIS 3 LINES OF CODE WHICH FILL MATRIX AND CREATE ARRAYS 
b = [[randint(1, 10) for i in range(1000)] for i in range(1000)]
c = [[[] for i in range(1000)] for i in range(1000)]



# BETTER AND FASTER VERSION
start1 = time()
for i in range(1000):
    for j in range (1000):
        c [i][j] = a[i][j] * b[i][j]
        
end1 = time()
print(end1-start1)


# SLOWER VERSION 
start2 = time()
for i in range(1000):
    for j in range (1000):
        c [j][i] = a[j][i] * b[j][i]
        
end2 = time()
print(end2-start2)

#############################################################################################################################################################################

