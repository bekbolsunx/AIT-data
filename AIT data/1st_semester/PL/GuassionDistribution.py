#22.11.2023


from random import randint 
from matplotlib import pyplot as plt
import math 

tmp = []
N = 200
arr = [0] * (N+1)
for i in range (100000):
    s = sum([randint(0,1)for j in range (N)])
    tmp.append(s)
    arr[s] += 1
    
avg = sum(tmp) / len(tmp)
var = sum([(avg - i )**2 for i in tmp])**0.5/N

arr2 = [0]*N
for x in range(N):
    arr2[x] = 1/(var*(2*math.pi))*math.exp2(-1/2*((x - avg)/var)**2)

# plt.plot(list(range(N + 1 )), arr)
plt.plot(arr2, color = 'green')
plt.show()