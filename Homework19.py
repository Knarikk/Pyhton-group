'''N1'''
# def fact(n):
#     fact = 1
#     for i in range(n,1,-1):
#         if( n!= 0):
#             fact *= i
#     return fact 

'''N2'''
# import math
# def area(r,h):
#     V = 2 * math.pi * r * h
#     A = 2 * math.pi * r * h + 2 * math.pi * r**2
#     return V,A
# print(area(2,2))


'''N3'''
# import math
# def func(r):
#     V = 4 / 3 * math.pi * r ** 3
#     A = 4 * math.pi * r ** 2
#     return (V,A)
# print(func(2))


# import math
# def radian(degree):
#     radian = degree * math.pi / 180
#     return radian
# print(radian(90))

'''Bubble Sort'''
# list1 = [10,75,43,15,25,-4,27,-1]
# for i in range(0,len(list1)-1):
#     for j in range(0,len(list1) - 1):
#         if list1[j] > list1[j+1]:   
#             list1[j],list1[j+1] = list1[j+1],list1[j]
# print(list1) 

'''Linear search'''

# def LinearSearch(list1,number):
#     for i in range(0,len(list1)):
#         if number == list1[i]:
#             return i
#     else:
#         return -1
# list1 = [10,15,20,25,30,45,60,75,85,95,100,155]
# print(LinearSearch(list1,85))

'''Binar search'''

# def BinarySearch(list1,number):
#     l = 0
#     r =len(list1) - 1
#     while(l <= r):
#         m = (l + r) // 2
#         if(list1[m] == number): 
#             return m
#         elif(number < list1[m]):
#             r = m - 1
#         else:
#             l = m + 1
#     return -1
# list1 = [10,15,20,25,30,45,60,75,85,95,100,155]
# print(BinarySearch(list1,85))

