#               #05.09.2023

# #код для проверки к примеру экзаменов или что то

# def fun1(x):
#     if x >80:
#         print("Passed")
#     else:
#         print("Lose")
# fun1(77)


# #Средние вычислить  число

# def avarage(b1,b2,b3,b4,b5,b6,b7,b8,b9):
#     return (b1+b2+b3+b4+b5+b6+b7+b8+b9) //  9
# result=avarage(17,16,17,26,22,28,30,21,18)
# print(result)


#         # 05.09.2023


# ages = [21,22,17,13]
# print (sum(ages) // len (ages))

# x = input("value1:")
# y = input("Value2:")

# print("sum is", int(x) + int(y))
# print("difference", int(x) - int(y))


# s="value"
# x=input(S)
# if (int(x)==90):
#     print("correct")
# else:
#     print("not correct")


# import random
# while True:
#         x = random.randint(100,200)
#         y = random.randint(500,800)
#         res = x+y
#         print(x,"+", y , "=")

#         volume = input("Answer is : ")
#         if(res==int(volume)):
#          print("Correct")

#         else:
#          print("Wrong")


#               06.09.2023


# n=0
# s=0
# while True:
#         op= input("add or substract(1,0)")
# if op=="1":
#           n= n+1
#           s= s + int(x)
# else:
#         n= n-1
#         s= s+int(x)


# x = input("age of new student:")
# s = s + int(x)
# n = n + 1

# print(s/n,s+n)


# arr = [3,5,6,9,5]

# print(arr[2:])
# print(arr[:2])
# print(arr[2])

# for a in arr :
#         print(a*a)


# arr = [1.3, 2.3, 1.7, 1.8, 1.9, 1.7]
# n = sum(arr) / len(arr)

# for a in arr:
#         if a >= n*1.2:
#                 print("higher", a )
#         if a <= n*0.8:
#                 print("lower", a )

# 07.09.2023

# Дабовление
# var = {"Geeks", "for", "Geeks"}
# var.add("bek")
# print(var)

# var.add("Daxit")
# for i in range (1,100):

#     var.add(i)

# #что то
# print("\nSet after adding element : ", end = "")
# print(var)


# Совмещает список , максимум 2 списка может
# people = {"Jay", "Abd", "Archi"}
# vampires = {"Karen", "July"}
# draculas = {"Loki", "Thyk"}

# population = people.union(vampires)
# print ("Union using union() function")
# print(population)

# population = people|draculas


# Диапазон 3 и 9 (в 6 range)
# set1 = set()
# set2 = set()

# for i in range (6):

#     set1.add(i)

# for i in range (3,9):
#     set2.add(i)

# set3 = set1.intersection(set2)

# print("Intersection using intersection()function")
# print(set3)

# #Диапазон пример 2 (вкратце)
# # set3 = set1 & set2
# print(set3)

# #Различие
# set1 = set()
# set2 = set()

# for i in range(5):
#     set1.add(i)

# for i in range(3,9):
#     set2.add(i)

# set3 = set1.difference(set2)

# print(" Difference of two sets using difference() function")
# print(set3)

# #Различие (вкратце) (работает одинаково)
# set3 = set1 - set2

# print("\nDifference of two sets using '-' operator")
# print(set3)


# #стирает СЕТ
# set1 = {1,2,3,4,5,6}

# print("Initional set ")
# print(set1)

# set1.clear()

# print("\nSet after using clear ()function ")
# print(set1)


# #Прибавление индекса
# a = [1,2,3,4,5,6,7,8,9,10]
# for i in range(len(a)):
#     if i < len(a)-1:
#         a [ i ] = a [ i ] + a [ i + 1 ]
# a[9] = a[9] + a[0]
# print (a)


# 11.09.2023 Emil classes
# Находим середину (median) в Arr
# arr = [1,7,3,1,5,4]

# def median(arr):
#     arr = sorted(arr)
#     print(arr)
#     mid=int(len(arr)/2)
#     if mid * 2 == len(arr):
#         return (arr[mid] + arr[mid-1]) / 2
#     else:
#         return arr[mid]
# print (median(arr))

# arr=[1,2,3,4,5,6]
# def swap(arr,a,b):
#     x=arr[a]
#     arr[a]=arr[b]
#     arr[b]=x
#     return arr
# print(arr)
# print(swap(arr, 2, 3 ))


# arr[0], arr[1] = arr[1] , arr[0]
# print(arr)

# arr1= [1,3,5,6]
# arr2 = [2,4,7]
# i = 0
# j = 0
# while i < len(arr1) and  j < len(arr2):
#     if arr1[i] < arr2[j]:
#         print(arr1[i])
#         i = i+1
#     else:
#         print(arr2[j])
#         j = j+1
# while j < len(arr2):
#     print(arr2[j])
#     j = j+1
# while i < len(arr1):
#     print(arr1[i])
#     i = i+1


# Специально выдать тот индекс тот который мы хотим
# arr= [3,5,6,8,10]
# i = 0
# while i < 4 :
#     print(arr[i])
#  i = i + 1


# 11.09.2023 # Munara classes
# возвращает сумму чисел от 1 до bek
# def sum(bek):
#     return bek* (bek + 1 ) /2
# print(sum(5000))

# 13.09.2023
# Emil classes

# Project with all tools which we used before
# arr = [[100,100],[1,2],[3,5],[3,4],[4,6],[5,4]]
# def avg2D(arr):
#     sx =0
#     sy =0
#     for i  in arr:
#         sx += i[0]
#         sy += i[1]
#     return sx/len(arr), sy/len(arr)

# def distance(p1,p2):
#     dx = (p1[0]-p1[0])
#     dy = (p1[1]-p1[1])
#     return(dx**2+dy**2)**0.5

# def get_max_index(arr):
#     mx = arr[0]
#     for i in arr:
#         if mx < i:
#             mx = i
#     return mx

# arr = [[100, 100], [1, 3], [3, 5], [4, 6], [5, 4]]
# m = avg2D(arr)
# d = []
# for i in arr:
#     dist = distance(i, m)
#     d.append(dist)

# print(arr)
# print(m)
# print(d)
# print(max(d))
# index = get_max_index(d)
# print(index)
# print(d[index])
# print(arr[index])


# #Cамая дальняя точка
# arr = [[100, 100], [1, 3], [3, 5], [4, 6], [5, 4]]


# def max_dist(arr):
#     s=[]
#     for i in range(len(arr)):
#         for j in range(i+1, len(arr)):
#             d = int(distance(arr[i],arr[j]))
#             s.append([i , j , d])
#         return s
# print(max_dist(arr))

# arr=[1,2,3,4,5,7,8,]
# def get_max_index(arr):
#     maxIND = 0
#     for i, val  in enumerate(arr):
#         if arr[maxIND] < val:
#             maxIND = i
#     return mx
# print(maxIND[i])

# 14.09.2023
# Munara Classes

# arr=[1,0,1,1]
# def convert_bek(arr):
#     decNum = 0

#     for i in range(len(arr)-1,-1,-1):
#         j = len(arr)-i-1
#         decNum +=2**i *arr[j]
#     return decNum
# print(convert_bek(arr))

# a=[1,0,1,1]
# def convertBinTolnt(a):
#     a=6
# def convertIntToBin(a):
#     digit1 = a mod 2
#         num1= a/2
#     digit2=num1 mod 2

#


# def has_word(s,x):
#     i = 0
#     for i in range(len(s)):
#         if x == s [i : i+len(x)]:
#             return True
#     return False

# x = "bek"
# s = "Emilbek bilgaziev"

# print(has_word(s,x))

# print(s.upper())
# print(s.split(' '))





##############################################################################################################################################################################





# 18.09.2023 Emil classes

# m = [0]
# n = 120
# p = 100
# k = 0.01
# for i in range (n):
#     x = p + m[1](1+k)
#     m.append (int(x))
# print(m)





##############################################################################################################################################################################






# 19.09.2023
# Функция для создания матрицы:
# def create_2d_mtrx(rows, cols):
#     a = [[1,0,2],[2,3,-1],[3,-2,0]]
#     b = [[4,1],[0,-3],[-1,1]]
#     arr = []
#     for i in range(rows):
#         col = []
#         for j in range(cols):
#             col.append(0)
#         arr.append(col)
#     return arr

# Расшифровка в for loop format

# print(set(arr1 + arr2))
# print( a & b ) = {2,3}
# print( a | b ) = {1,2,3,4}
# print( a - b ) = {1}
# print( b - a ) = {4}

# arr1 = [1,2,3,1,2]
# arr2 = [2,3,4,4]

# x = set()
# for i in arr1:
#     x.add(i)
# for j in arr2:
#     x.add(j)
# print(x)






##############################################################################################################################################################################






# 20.09.2023
#Dice probablity
# from random import randint

# arr = [0] * 13
# varr = [0,0,1,2,3,4,5,6,7,6,5,4,3,2,1]
# N = 10000000
# for i in range(N):
#     d1 = randint(1, 6)
#     d2 = randint(1, 6)
#     d = d1 + d2 
#     arr[d] += 1
# for j,v in zip(arr,varr):
#     print(i / N, v/36)

#Get random integers in range of 10

# arr = [randint(0,10) for i in range(10)]

#Find  same val and print with their indexes 
# arr1 = [2,3,5,6]
# arr2 = [1,4,2,5]
# arr3 = []
# for i, val1 in enumerate(arr1):
#     for j, val2 in enumerate(arr2):
#         if val1 == val2 : 
#             arr3.append([i,j])
# print(arr3)
       
#IN SHORT      
# arr4 = [[i, j] for i, va1 in enumerate(arr5) for j, va2 in enumerate(arr6) if va1 == va2]
# print(arr4)





##############################################################################################################################################################################






#21.09.2023

#Convert decimal num to binory num 
# def convertDecToBin(n):
#     binArray=[]
#     while(n!=0):
#         binArray.append(n%2)
#         n=n//2
        
#     return binArray[::-1]
# print (convertDecToBin(11)) #1011

# def convertDecToBin(n):
#     binArray=[]
#     while(n!=0):
#         binArray.append(n%2)
#         n=n//2
        
#     return binArray[::-1]
# print (convertDecToBin(10)) #1010

#Convert binory num to decimal num
# def convertBinToDec(arr):
#     size = len(arr)
#     sum = 0 
#     for i in range(size):
#         sum = sum + 2 ** (size-i-1)*arr[i]




##############################################################################################################################################################################




#25.09.2023

# from random import randint

# val1 = randint(0,10)
# val2 = randint(0,10)

# s = f"{val1} + {val2} = {val1+val2}"

# print(s)

# fb = open()






##############################################################################################################################################################################






#26.09.2023

# def longest_word_with_loop(words):
#     longest = " "
#     for word in words:
#         if len(word) > len(longest):
#             longest = word
#     return longest

# fb = open(f'C:/Users/bekbo/OneDrive/Desktop/TysonMike.txt', 'r')
# line = fb.read()
# words = line.split()

# longest1 = longest_word_with_loop(words)
# print(longest1)
# fb.close()





##############################################################################################################################################################################






#27.09.2023 
# Permutation 

# def factorial(s,i):
#     if i == len(s):
#         print('',join(s))
#     for i in range(i,len(s)):
#         s[a] , s[i] = s[i] , s[a]
#         fractional (s, i + 1)
#         s[a] , s[i] = s[i] , s[a]
        
# s = 'ABC'    
# bek(list(s),0)

#in short (Permutation)
# from itertools import permutations

# s = "123"
# for i in permutations(list(s)):
#     print(i)

# arr = [3,2,1,4]


# def move_even_num(arr):
#     a = []
#     q = 0
#     p = len(arr) - 1
#     for i in arr:
#         if i%2 == 0:
#             a[q] = i
#             q += 1
#         else:
#             a[p]=i
#             p += -1
#     return arr


#02.10.2023   PROBABLITY AND STAT
#Combination (when order is important) #10
# arr = [0 , 1 , 2 , 3 , 4 , 5]

# for i in arr:
#     for j in arr:
#         for k in arr:
#             if i < j < k:
#                 print(i,j,k)
            
#Combination ALL (when order is NOT important) #125
# for i in arr:
#     for j in arr:
#         for k in arr:
#             print(i,j,k)

#Permuntations #60
# n = 0 
# for i in range (0,5):
#     for j in range (0,5):
#         for k in range (0,5):
#             if not (i == j or j ==k or i ==k):
#                 n += 1
#                 print(i,j,k)
# print('total permuntation:' , n)





##############################################################################################################################################################################





### 11.10.2023


# def factorial(n):
#     x = 1 
#     for i in range(1, n + 1):
#         x = x * i 
#     return x 
# print(factorial(6))


# def permuntation(n,k):
#     bek = factorial(n) / factorial(n - k)
#     return bek 
# print (permuntation(10,5))
    

# def combination(n,k):
#     sek = factorial(n) /    (factorial(n - k) * factorial(k))
#     return sek
# print(combination(10,5))

### Recrusion
# a = len(a)
# arr = ['google']
# def rep_per(arr):
#     s = []
#     for i in arr: 
#         if i not in s: 
#             s.append(i)
    
   
# def permute(s, i):
#     if i == len(s):
#          print(''.join(s))

#     for x in range(i, len(s)):
#         s[x], s[i] = s[i], s[x]
#         permute(s, i + 1)
#         s[x], s[i] = s[i], s[x]
# permute(s, 0)
    
    ### itarative method 
    ### суммируем его с предыдущим 
# num1 = 0 
# num2 = 1

# for i in range(0,9): 
#     num3 = num1 + num2
#     num1 = num2 
#     num2 = num3
# print(num3)

     ### Itarative method 
     
# b = [0,1]

# for i in range(9):
#     b.append(b[-1]+b[-2])
# print(b)
# print(b[-1])

     ### Above RECRUSION METHOD 
     
# def febonachi(n):
#     if n <= 0:
#         return 0 
#     elif n == 1:
#         return 1
#     else:
#         return febonachi(n-1) + febonachi(n-2)
# print(febonachi(10))





##############################################################################################################################################################################





### Math quiz 16.10.2023


# from random import randint

# count_true = 0
# count_false = 0

# while True:
    
#     print(f'Число правильных -',count_true)
#     print(f'Число ошибок -',count_false)

#     try:
        
#         ops = "+-/*"
#         id = randint(0,3)
#         a = randint(0,10)
#         b = randint(0,10)
        
#         if ops[id] == "/":
#             c = int(input(f"{a*b} {ops[id]} {b} = "))
#             if c == a:
#                 count_true += 1
#                 print("Chetko")
#             else:
#                 count_false += 1
#                 print("Ты попутал")
#             continue
        
#         c = int(input(f"{a} {ops[id]} {b} = "))
#         if a-b == c and ops[id] == "-":
#             count_true += 1
#             print("Chetko")
#         elif a+b == c and ops[id] == "+":
#             count_true += 1
#             print("Chetko")
#         elif a*b == c and ops[id] == "*":
#             count_true += 1
#             print("Chetko")
#         else:
#             count_false += 1
#             print("Ты попутал ")
#     except ZeroDivisionError:
#         print("Ты че э ? на ноль не делиться  ?!")
#     except ValueError:
#         print("Д*бил ты буквами используешь!")
        
        
        
        
        
##############################################################################################################################################################################




### 18.10.2023 p/s
                 #variance



# x = [17, 17, 19, 23, 19, 18, 26, 17, 17, 18, 19]

# y = [65, 55, 30, 27, 25, 35, 47, 30]

# # average
# avg = sum(x) / len(x)

# # variance
# var = sum([(avg - i) ** 2 for i in x]) / len(x)

# # std
# print(var**0.5)

# # average
# avg = sum(y) / len(y)






##############################################################################################################################################################################






### 19.10.2023

# 1111 -> 0000
# def complement(a):
#     a = [int(i) for i in a]
#     ln = len(a)
#     for i in range(ln):
#         a[i] = 0 if a[i] == 1 else 1
#     return a


# print(complement([1, 0, 1]))
# print(complement("101"))

   
# ab#c -> ac
# def backspace(s):
#     out = ""
#     ln = len(s)
#     for i in range(ln):
#         if s[i] == "#":
#             out = out[: len(out) - 1]
#         else:
#             out += s[i]
#     return out


# is backspace(ab#c) == backspace(ad#c)
# def is_same(s1, s2):
#     return backspace(s1) == backspace(s2)


# s = "baab##c"
# t = "baad##c"
# print(is_same(s, t))






##############################################################################################################################################################################







###    23.10.2023
## Programming lenguage 

# x = [17, 17, 19, 18, 23, 19, 18, 26, 17, 17, 18, 16, 20, 21]
# y = [30, 47, 35, 27, 30, 55, 65]

#x
# average
# avgX = sum(x) / len(x)
# variance
# varX = sum([(avgX - i) ** 2 for i in x]) / len(x)
# std
# print("X array - ",varX**0.5)
#y
# average
# avgY = sum(y) / len(y)
# variance
# varY = sum([(avgY - i) ** 2 for i in y]) / len(y)
# std
# print("Y array - ",varY**0.5)

# variance
# def variance_two_arr(varX,varY):
#     if varX == varY:
#         return True
#     else:
#         return False  
# print(variance_two_arr(varX,varY))

# average
# def avg_two_arr(avgX,avgY):
#     if avgX == avgY:
#         return True 
#     else:
#         return False
# print(avg_two_arr(avgX,avgY))


#Задача из мировой олимпиады)
# m**2 = n + 2
# n**2 = m + 2
#4mn - n**3 - m**3 = ?

#Способ как решить через программу 
# for n in range(100000):
#     for m in range(100000):
#         if(m**2 == n+2 and n**2 == m+2):
#             print(4*m*n - n**3 - m**3)
            
##############################################################################################################################################################################

            ### 23.10.2023
            # Into to Comp Science 
            
# import time

# # get the start time
# st = time.time()

# # main program
# # find sum to first 1 million numbers
# sum_x = 0
# for i in range(1000000):
#     sum_x += i

# # wait for 3 seconds
# time.sleep(6)
# print('Sum of first 1 million numbers is:', sum_x)

# # get the end time
# et = time.time()

# # get the execution time
# elapsed_time = et - st
# print('Execution time:', elapsed_time, 'seconds')



# arr = [4,3,5,8,9,5,3,2,5]




# arr1 = [1,2,3,3,3,4,4]
# arr2 = [3,3,3,4,4,4,2,2,2,2]
# arr3 = []

# d1 = {}
# d2 = {}
# d3 = {}

# for i in arr1:
#     if i in d1:
#         d1[i] += 1 
#     else:
#         d1[i] = 1
        
# for j in arr2:
#     if j in d2:
#         d1[j] += 1 
#     else:
#         d1[j] = 1
        
# arr3 = arr1 + arr2

# for k in arr3:
#     if k in d3:
#         d3[k] += 1 
#     else:
#         d3[k] = 1

# print(d3)


### 24.10.2023

# from time import time 
# from random import randint
# arr = [randint(0,10) for i in range(1000000)]
# arr = arr + [20,20]

# d = {}

# tic = time()



# toc = time()
# print(toc-tic)






##############################################################################################################################################################################






#With String 
# def palindrome(n):
#     s = str(n)
#     if n < 0:
#         return False
#     elif int(s[::-1]) == n:
#         return True 
#     return False 
        
# print(palindrome(12321))


#with int

# def is_palindrome(num):
#     s = str(num)
#     x, y = 0, len(s) - 1
    
#     while x <= y:
#         if s[x] != s[y]:
#             return False
#         x += 1
#         y -= 1
    
#     return True

# print(is_palindrome(123321))
# print(is_palindrome(1234))

# def roman_to_int(s):
#     roman_values = {
#         'I': 1,
#         'V': 5,
#         'X': 10,
#         'L': 50,
#         'C': 100,
#         'D': 500,
#         'M': 1000
#     }

#     result = 0
#     prev_value = 0

#     for char in s[::-1]:  # Iterate the string in reverse order.
#         current_value = roman_values[char]
        
#         if current_value < prev_value:
#             result -= current_value
#         else:
#             result += current_value
        
#         prev_value = current_value

#     return result

# # Example usage:
# s1 = "III"
# print(roman_to_int(s1))  # Output: 3

# s2 = "ML"
# print(roman_to_int(s2))  # Output: 40

# s3 = "MCMXCIV"
# print(roman_to_int(s3))  # Output: 1994






##############################################################################################################################################################################







# # Home work 

# # Question 1 
# print("1 - Question ")
# n1=234
# n2=4421
# def difference(n):
#     a=n
#     y=1
#     x=0
#     while a>0:
#         k=a%10
#         y=y*k
#         x+=k
#         a=a//10
#     return y-x
# print(difference(n1))
# print(difference(n2))


# # Question 2 
# print("2 - Question ")
# def convertDecToBin(n):
#     binArray=list()   
#     while(n!=0):
#         rem=n%2
#         n=n//2
#         binArray.append(rem)
#     while len(binArray)<4:
#         binArray.append(0)
#     return binArray[::-1]
# def xor_operation(n1,n2):
#     a=convertDecToBin(n1)
#     b=convertDecToBin(n2)
#     xor_results=[]
#     for i in range(len(a)):
#      xor_results.append(a[i]^b[i])
#     return xor_results 
# print(xor_operation(11,5))

# # Question 3 
# print('3 - Question')
b1=[1,4,6,6,7,8,10,11]
b2=[2,4,5,9]
def mergeSORTED(b1,b2):
    b3=[]
    i=0
    j=0
    while i<len(b1) and j<len(b2):
        if b1[i]<b2[j]:
            b3.append(b1[i])
            i+=1
        else:
            b3.append(b2[j])
            j+=1
    b3+=b1[i:]
    b3+=b2[j:]
    return b3
print(mergeSORTED(b1,b2))

# # Question 4 
# print('4 - Question')
# def blackWHITE(coordin):
#     nums="12345678"
#     letters="abcdefgh"
#     a=0
#     b=0
#     for i in range(len(letters)):
#       if coordin[0]==letters[i]:
#         if i%2==0:
#          a=False
#         else:
#           a=True
#       if coordin[1]==nums[i]:
#         if i%2==0:
#           b=False
#         else:
#           b=True
#     return a^b
# print(blackWHITE("b8"))






##############################################################################################################################################################################





# 31.10.2023 discrete math 

# def find_prime(n):
#     ns = int(n**0.5) #Sqrt root 
#     primeARR = [ 2 , 3 , 5 , 7 , 11 ]
#     for i in primeARR:
#         if ns > i  and n % i == 0:
#             return False
#         return True
# print(find_prime(101))


# def factor(n):
#     d = {}
#     primes = [2 , 3 , 5 , 7 , 11]
#     if find_prime(n):
#         return {n : 1}
#     while n > 1:
#         for i in primes:
#             if n % i == 0:
#                 if n not in d:
#                     d[i] = 0 
#                 d[i] += 1
#                 n /= i
#                 brek
#     return d 
    
# print(factor(23))







##############################################################################################################################################################################






# # 01.11.2023 programing lenguage 

# class Group():
#     def __init__(self, group_name, creation_date):
#         self.group_name = group_name
#         self.creation_date = creation_date
#         self.members = []
#         self.admins = []
#         self.messages = []  # List to store messages

#     def add_member(self, member_name):
#         if member_name not in self.members:
#             self.members.append(member_name)

#     def remove_member(self, member_name):
#         if member_name in self.members:
#             self.members.remove(member_name)

#     def add_admin(self, admin_name):
#         if admin_name not in self.admins:
#             self.admins.append(admin_name)

#     def remove_admin(self, admin_name):
#         if admin_name in self.admins:
#             self.admins.remove(admin_name)

#     def display_group_info(self):
#         print()
#         print(f"Group Name: {self.group_name}")
#         print(f"Creation Date: {self.creation_date}")
#         print("Members:", self.members)
#         print("Admins:", self.admins)
#         print("Messages:")
#         for i, message in enumerate(self.messages, start=1):
#             print(f"{i}. {message}")
#         print('***********************')

#     def send_message(self, sender, message):
#         if sender in self.members:
#             self.messages.append(f"{sender}: {message}")
#         else:
#             print("Only group members can send messages.")


# ait_group = Group("AIT_Group", "01,11,2023")
# ait_group.add_member("Alina")
# ait_group.add_member("Dayana")
# ait_group.add_member("Jenish")
# ait_group.add_member("Bek")
# ait_group.add_admin("Uluk")
# ait_group.add_admin("Alina")

# ait_group.display_group_info()

# ait_group.send_message("Alina", "Hello, everyone!")
# ait_group.send_message("Bek", "Hi, Alina!")

# ait_group.display_group_info()

# ait_group.send_message("Non-Member", "This message should not be sent.")

# ait_group.remove_member("Bek")
# ait_group.display_group_info()


# Topic CLASSES in python 
# class NPC():
#     def __init__(self, hp , speed , demage):
#         self.hp = hp
#         self.speed = speed 
#         self.demage = demage 
#     def double_speed(self):
#         self.speed *= 2
        
# warrior = NPC(40,90,100)
# ninja = NPC(20,80,70)

# print(f"warrior speed: {warrior.demage}")
# print(f"warrior speed: {warrior.hp}")
# print(f"warrior speed: {warrior.speed}")
# print(f"ninja speed: {ninja.speed}")
# warrior.double_speed()
# ninja.double_speed()
# print(f"warrior speed: {warrior.speed}")
# print(f"ninja speed: {ninja.speed}")





##############################################################################################################################################################################





# # 14.11.2023 discrete math
# def euclidean_algorithm(a, b):
#     while b:
#         a, b = b, a % b 
#     return a

# # Example usage:
# num1 = 666
# num2 = 558

# gcd = euclidean_algorithm(num1, num2)

# print(f"The GCD of {num1} and {num2} is: {gcd}")





##############################################################################################################################################################################







#EXAM in 14.11.2023

# arr = [5,4,3,6,1,8,2,0]

# def get_min_index(arr):
#     min_index = 0 
#     for i , val in enumerate(arr):
#         if arr[min_index] > val:
#             min_index = i
#     return min_index 

# print(f'It is an index of min val:', get_min_index(arr))

# def get_max_index(arr):
#     max_index = 0 
#     for i , val in enumerate(arr):
#         if arr[max_index] < val:
#             max_index = i 
#     return max_index
# print(f'It is an index of max val:',get_max_index(arr))

# def swap(arr):
#     arr[get_min_index(arr)] , arr[get_max_index(arr)] = arr[get_max_index(arr)] , arr[get_min_index(arr)]
#     return arr 
# print (swap(arr))








##############################################################################################################################################################################






#как идет подсчт кредитов (в сша )

# def calculate_monthly_payment(loan_amount, annual_interest_rate, loan_term_months):
#     monthly_interest_rate = (annual_interest_rate / 100) / 12
#     numerator = loan_amount * monthly_interest_rate * (1 + monthly_interest_rate) ** loan_term_months
#     denominator = (1 + monthly_interest_rate) ** loan_term_months - 1
#     monthly_payment = numerator / denominator
#     return monthly_payment

# # Ваш пример
# loan_amount = 120000
# annual_interest_rate = 30
# loan_term_months = 12

# monthly_payment = calculate_monthly_payment(loan_amount, annual_interest_rate, loan_term_months)
# print(f"Ежемесячный платеж: {round(monthly_payment, 2)} сом")

# Кредиты в КР (как СЧИТАЮТ)
# m = 12000
# count = 0 
# b = 120000
# i = (30/100)/12

# while b >= 0:
#      b = b*(1+i) - m
#      count += 1 
# print (count)








##############################################################################################################################################################################











#  Correlation coefficient
# arrA = [1000000,900000,1100000,1000000,1000000,800000]
# arrB = [-1000,900,-10000,950,1000,800]

# def r (arrA , arrB):
#      a_cap , b_cap = sum(arrA) / len(arrA), sum(arrB) / len(arrB)
#      up = 0
#      down = 0
#      down1 = 0 
#      for a , b in zip(arrA,arrB):
#           up += (a-a_cap)*(b-b_cap)
#           down += (a-a_cap)**2 
#           down1 += (b-b_cap)**2
#      return up/(down *down1)**0.5
# print(r(arrA,arrB))








##############################################################################################################################################################################








# class SubstituteCipher():
#      def __init__(self, s):
#           self.s = s 
#           self.new_str =''
#           self.start = ord('a')
#           self.end = ord('z')
          
          
#      def cipher(self):
#           for i in self.s:
#                if ord(i) + 13 <= self.end:
#                     self.new_str += chr(ord(i)+13)
#                if ord(i) + 13 >self.end:
#                     self.new_str += chr(ord(i)+ 13 - 26)
                    
#      def show(self):
#           return self.new_str
                    
# hello = SubstituteCipher('beksteel')
# hello.cipher()
# print(hello.show())
          
          
          
          
          
##############################################################################################################################################################################
#1

# arr = [2, 4, 5, 6, 7, 2, 2, 1]

# def average(arr):
#     s = 0
#     i = 0

#     while i < len(arr):
#         s += arr[i]
#         i = i + 1

#     return s / i

# res = average(arr)
# print(res)

          
#2

         
# def get_max_index(arr):
#      mx = 0 
#      for i , val in enumerate(arr):
#           if arr[mx] < val:
#                mx = i 
#      return mx

# arr = [1,2,3,0,2]
# res = get_max_index(arr)
# print(res)





##############################################################################################################################################################################




# # МЕТОД цепочки 
# def fib( n ):
#      print("n=", n)
#      # Бесконечность  ДОЛГИЙ МЕТОД
#      # if n <= 1:
#      #      return n
#      # By dictionary
#      if n in d:
#           return d[n]
     
#      d[n] =  fib(n-1, d) + fib(n-2 , d)
#      return d[n]

# d={0:0 , 1:1}
# print(fib(8))







####################################################################################################################################################################################################




n = 1000000
arr = [n]

def sort(arr):
     if len(arr)==1 or len(arr)==0:             ##ЭТО ОСТОНАВЛИВАЕТ РАБОТУ for loop для испл func
          return arr

     last = arr[-1]                 ## You can use any number , it's doesn't matter 

     right = []               ##It's our arrays which we will use to store results 
     left = []
     middle = []
     
     for i in arr:            ##There is a lines of code which appends by the condition.
          if i > last:
               right.append(i)
          if i <last:
               left.append(i)
          if i == last:
               middle.append(i)

     return sort(left)+middle+sort(right)         ##There is we join our massive for get result , and also we use our function to to sort them. Also we reuse sort function to left and right for correct result.


# print('original arr = ', arr)
# print('sorted arr = ', sort(arr))








###################################################################################################################################################################################################################################################################################################################################################





# # Recursive method 

# 1) base case 2) recursive case 

# # 0 is water and 1 is a island , find and count islands 

# def check_border(h , w , r , c): # this lines of code checks a boreders 
#      return 0 <= r < h and 0 <= c < w 


# def island(arr , i , j , memory):
#      arr[i][j] = 0
#      # memory.add((i,j))
#      for x , y in [(i-1 , j+0 ),(i+1 , j+0) , (i-1 , j+0),(i+0 , j+1)]: # This comands gives navigation of 4 sides
#           if check_border(arr , r ,c) and arr[r][c] == 1:
#                island(arr , r , c , memory)
               
# count = 1
# memory = set()
# for i in range(len(arr)):
#      for j in range(len(arr[i])):
#           if arr[i][j] == 1:
#                island(arr, 0 , 0,memory )
#                count += 1     
               
               
##       EXAM          SUM  with recursive method 
# def sum(n):
#      if n == 1 or n == 0:
#           return  n
#      return sum(n-1)+n 
# print(sum(0))
     
     
########################################################################################################################################
# ПРИМЕРНО ТАКОЙ БУДЕТ НА МИДТЕРМЕ 


# balance = 100000
# payment = 2000
# interest = 22

# month_interest = interest / 12 / 100
# cnt = 0
# a = 0
# while balance > 0:
#     cnt += 1
#     balance += balance * month_interest
#     a += balance * month_interest
#     balance -= payment
#     print(
#         cnt,
#         round(balance * month_interest),
#         round(payment - balance * month_interest),
#         round(balance),
#     )
# print(cnt, a)
########################################################################################################################################

### PERMUTATIONS
# def my_permute(s, i):
#     if i == len(s):
#         # print(''.join(s))
#         x = ''.join(s)
#         if 'iu' not in x and 'ui' not in x:
#             print(x)
    
#     for a in range(i, len(s)):
#         s[a], s[i] = s[i], s[a]
#         my_permute(s, i+1)
#         s[a], s[i] = s[i], s[a]
        

# s = 'quiz'
# my_permute(list(s),0)

# def min_val(arr):
#     mn = arr[0] 
#     for i in arr:
#         if i < mn: # max is : if i > mx
#             mn = i
#     return mn

    
# def factorial(n):
#     if n == 0 or n ==1:
#         return 1
#     else:
#         return n * factorial(n-1)
    
# def max_index():
#     mx = 0
#     for i , val in enumerate(arr):
#         if arr[mx] < val: # min is : arr[mn] > val:
#             mx = i
#     return mx 


########################################################################################################################################
# arr1 = [6,13,12]
# arr2 = [1,2,3,4,5,6,10,11]
# # print(sorted(arr1 + arr2))


# arr = [1, 2, 3, 5, 6, 7]



# def get_value_index(arr,value):
#      index = -1                          # -1 its means false
#      for i,val in enumerate(arr):
#           if value == val:
#                index = i
#      return index

# print(get_value_index(arr,3))

########################################################################################################################################


# def max_recursive(arr):
#      if len(arr) == 0:
#           return []
#      if len(arr) == 1:
#           return arr[0]
#      else:
#           m = max_recursive(arr[1:])
#           return m if m > arr[0] else arr[0]
# print(max_recursive([1,3,4,5,6,3,2,9]))

# ########################################################################################################################################
# ####     MIDTERM PL      (EMIL AGAY'S CODE )
# from collections import defaultdict

# class Sessions:
#     def _init_(self, start, end, mid, max_count = 50):
#         self.start = start
#         self.end = end
#         self.mid = mid
#         self.max = max_count

#     def add_person(self, pid):
#         if len(self.audience) < self.max:
#             self.audience.appen(pid)
#             return True
#         else:
#             return False

#     def count(self):
#         return len(self.audience)

# class Person:
#     def _init_(self, name, taino):
#         self.name = name
#         self.taino = taino

# class Movie:
#     def _init_(self, name, duration):
#         self.name = name
#         self.duration = duration

# class Kassa:
#     def _init_(self):
#         self.sessions = defaultdict(int)

#     def add_new_session(self, start, end, mid):
#         self.sessions[len(self.sessions)] = Sessions(start, end, mid)

#     def delete_session(self, sid):
#         del self.sessions[sid]

#     def sell_ticket(self, pid, sid, type):
#         if self.sessions[sid].add_person(pid):
#             print("Successfully sold the ticket")
#         else:
#             print("This session is full")

#     def add_movie(self, movie_name, duration):
#         self.movies[len(self.movies)] = Movie(movie_name, duration)

#     def add_new_member(self, name, tal_number):
#         self.members[len(self.members)] = Person(name, tal_number)

#     def total_sold_ticket(self):
#         return sum([session.count() for sid, session in self.sessions.items()])

#     def total_sold_tickets_for_session(self, sid):
#         return self.sessions[sid].count()



########################################################################################################################################




arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]


# get minimum value
def min_value(arr):
    mn = arr[0]
    for x in arr:
        if x < mn:
            mn = x
    return mn
# print(min_value(arr))


def max_value(arr):
    mx = arr[0]
    for i in arr:
        if i > mx:
            mx = i
    return mx
# print(max_value(arr))


def get_max_index(arr):
    mx = 0
    for i, val in enumerate(arr):
        if arr[mx] < val:
            mx = i
    return mx
# print(get_max_index(arr))

def sumB(arr):
    s = 0
    for i in arr:
        s += i
    return s
# print(sumB(arr))

def avg(arr):
    return sumB(arr) // len(arr)

# print(avg(arr))

def find_val_index(arr):
    target = 90
    
    for i , val in enumerate(arr):
        if val == target:
            return i
    return -1 # arr don't have this value.
# print(find_val_index(arr))



########################################################################################################################################

# #33
# x = 4
# y = 5
# a = 200

# b = x-y # ее ставим вне функции и это уже оптимизация 

# while (a>0):
#     if a%b==0:
#         print(a)
#     a-=1
    
# import time
# # здесь убрали a переменную и все резко в return 
# def sumMatrix(x, y):
#     return [[j + i for i in range(x)] for j in range(y)]

# start_time = time.time()

# result = sumMatrix(10, 10)

# end_time = time.time()

# elapsed_time = end_time - start_time 
# print(f"Время выполнения: {elapsed_time} секунд")


########################################################################################################################################



# #discrete math 
# class UserStorage:
#     def __init__(self, capacity=100):
#         # Constructor method for initializing the UserStorage object
#         self.capacity = capacity
#         #Pre-allocation . It's ensures that we have enough memory to store data.
#         self.usernames = [None] * capacity  # List to store usernames
#         self.passwords = [None] * capacity  # List to store corresponding passwords

#     def hash_function(self, username):
#         # Basic hash function: sum ASCII values of characters
#         # Function ord return ASCI value of char.For each character in ' username '
#         # And we use % (modulo)to ensure that the result of val falls within the  range of the hash table's capacity. 
#         return sum(ord(char) for char in username ) % self.capacity

#     def add_user(self, username, password):
#         # Calculate the index using the hash function.
#         # This index represents the initial position where the user's information will be stored in the usernames and passwords lists.
#         index = self.hash_function(username)

#         # Linear probing . We use is not 
#         while self.usernames[index] is not None:
#             index = (index + 1) % self.capacity

#         # Add the user to the storage
#         self.usernames[index] = username
#         self.passwords[index] = password

#     def delete_user(self, username):
#         # Find the index of the user and set their information to None
#         index = self.find_user_index(username)
#         if index is not None:
#             self.usernames[index] = None
#             self.passwords[index] = None

#     def get_password(self, username):
#         # Find the index of the user and return their password (or None if not found)
#         index = self.find_user_index(username)
#         return self.passwords[index] if index is not None else None

#     def find_user_index(self, username):
#         # Find the index of the user using the hash function and linear probing
#         index = self.hash_function(username)

#         while self.usernames[index] is not None:
#             # Check if the username matches at the current index
#             if self.usernames[index] == username:
#                 return index
#             index = (index + 1) % self.capacity

#         # User not found
#         return None

# # Example usage:
# user_storage = UserStorage()

# user_storage.add_user("Alice", "password123")
# user_storage.add_user("Bob", "secure_pass")

# print(user_storage.get_password("Alice"))  # Output: password123
# print(user_storage.get_password("Bob"))    # Output: secure_pass

# user_storage.delete_user("Alice")

# print(user_storage.get_password("Alice"))  # Output: None (user not found)


########################################################################################################################################
# def stars(init_num):
#     for i in range(init_num,0,-1):
#         print('*' * i)
    
# print(stars(7))
########################################################################################################################################
