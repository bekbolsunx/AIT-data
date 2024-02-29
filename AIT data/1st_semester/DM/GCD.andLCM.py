#     # Euclid algo
# def euclid_algo(a , b ):
#     while b:
#         a , b = b , a%b
#     return a 
# num1 = 150
# num2 = 80
# gcd = (euclid_algo(num1,num2))
# print(f'gcd of {num1} and {num2} is : {gcd}')

#  # In recursive method 
# def rec_euclid_algo(a, b ):
#     if  b == 0:
#         return a 
#     else:
#         return rec_euclid_algo(b, a%b)

# num1 = 287
# num2 = 91
# gcd = (rec_euclid_algo(num1,num2))
# print(f'gcd of {num1} and {num2} is : {gcd}')


# #     # LCM 
# from collections import defaultdict

# def factorize(n):
#     ans=defaultdict(int)
#     prime_array=[2,3,5,7,11,13,17,19]
#     for i in prime_array:
#         while n%i==0:
#             ans[i]+=1
#             n/=i
#     return ans

# def lcm(n1,n2):
#     n1f=factorize(n1)
#     n2f=factorize(n2)
#     d=n1f.keys()|n2f.keys()
#     ans=1
#     for i in d:
#         ans*=i**max(n1f[i],n2f[i])
#     return ans

# print(lcm(12,9))

