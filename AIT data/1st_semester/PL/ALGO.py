#4 n log n 
from time import time 
from random import shuffle

n =10 
n1 = 100
n2 = 10000
n3 = 1000000
n4 = 1000000000
# O n 
start = time()
arr = [i for i in range(n3)]
end = time()
print(end-start)
# start = time()

# # shuffle(arr)

# def sort(arr):
#      if len(arr)==1 or len(arr)==0:             ##ЭТО ОСТОНАВЛИВАЕТ РАБОТУ for loop для испл func
#           return arr
#      last = arr[-1]                 ## You can use any number , it's doesn't matter 
#      right = []               ##It's our arrays which we will use to store results 
#      left = []
#      middle = []
#      for i in arr:            ##There is a lines of code which appends by the condition.
#           if i > last:
#                right.append(i)
#           if i <last:
#                left.append(i)
#           if i == last:
#                middle.append(i)
#      return sort(left)+middle+sort(right)         ##There is we join our massive for get result , and also we use our function to to sort them. Also we reuse sort function to left and right for correct result.

# # sort(arr)
# end = time()
# # print(end-start)

# 2 binary search

def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid

        elif arr[mid] < target:
            left = mid + 1

        else:
            right = mid - 1

    
    return -1


start = time()

binary_search(arr,6)

end = time()
print(end-start)



# 4 (2 loops)
# start = time()

# for i in arr:
#     for j in arr:
#         pass
    
# end = time()

# print(end - start)
start = time()
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

fibonacci(30)
end = time()
print(end - start)

#7 n!

# start = time()
# def permutations(lst, start=0):
#     if start == len(lst) - 1:
#         # print(lst)
#         pass

#     for i in range(start, len(lst)):
#         lst[start], lst[i] = lst[i], lst[start]  # swap
#         permutations(lst, start + 1)
#         lst[start], lst[i] = lst[i], lst[start]  
        
# permutations(arr)
# end = time()
# print(end-start)


N = [1 , 10 , 100 , 10**3 , 10**4 , 10**6 , 10**9]

for n in N:
    arr = {i:True for i in range(n)}
    
    x = n-1
    start = time()
    for i in arr:
        if x == i:
            pass 
    end = time()
    print(n , end - start)