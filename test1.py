# x = 9
# print(x)
# y = 10
# print(y)
# z = 15
# print(z)

# res = []
# list1 = [1,2,3,5,7,6,3,2,5,10,15,25,20,19,17]
# for i in range(1,len(list1)-1):
   
    
#     if (list1[i-1] < list1[i] and list1[i] > list1[i+1]) or list1[i-1] > list1[i] and list1[i] < list1[i+1]:
#         res.append(list1[i])
# print(res)

# mydict = {
#     'D':56,
#     'E':12,
#     'F':69,
#     'C':45,
#     'B':23,
#     'A':67

# }

# dict1 = {}

# list1 = sorted(mydict,key = mydict.get,reverse = True)[:3]
# print(list1)    
# list2 = sorted(mydict.values(),reverse=True)[:3]
# print(list2)
# for x,y in zip(list1,list2):
#     dict1.setdefault(x,y)
# print(dict1)


#lesson14
# def calculator(a,b,gorc):
#     if gorc == '+':
#         return a+b
#     elif gorc == '-':
#         return a - b
#     elif gorc == '/':
#         return a / b
#     elif gorc == '*':
#         return a * b

# a = int(input('a= '))
# b = int(input('b= '))
# gorc = input()
# print(calculator(a,b,gorc))


# def func(mylist):
#     sum = 0
#     for i in mylist:
#         sum += i
#     return sum
# mylist = [1,2,3,4]
# print(func(mylist))


# def func(mylist):
#     mul = 1
#     for i in mylist:
#         mul *= i
#     return mul
# mylist = [2,3,4]
# print(func(mylist))


# def func(string):
#     count = 0
#     sum = 0
#     for i in string:
#         if i.isdigit():
#             count += 1
#             sum += int(i)
#     print(' count= ',count)
#     print('sum = ',sum)

# string = 'deds1232'
# func(string)

# x =lambda a,b:a+b
# print(x(5,2))




# def decorator_func(x):
#     def gorcoxutyun(list1):
#         return[x(i[0],i[1]) for i in list1]
#     return gorcoxutyun

# @decorator_func
# def func(a,b):
#     return a+b
# print(func([(5,3),(7,2)]))


# def  fib(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)
# print(fib(9))


#dekoratory funkcia a vory yndgrkum e ayl funkcia kody yndlaynelu hamar
# #inch e funkcian, rekursian
# funckian obyekt e vory yndunum e argumnetner ev veradardznum arjeq,
# kam cragrayin kodi mi mas e vorin kareli e dimel cragri mek ayl vayri.

#lesson 15


# str = 'python'
# for i in range(0,len(str)+2):
#     print(str[i])

#  print('y')

# print(y)

# str = 'frfrf'
# for i in range:
#     i += 1
#     print(i)

# print(1 / 0)

# dict1 = {'a': 1,'b': 2}




# a = 1
# b = 2
# s = a * b * sqrt(a)
# print(s)

# import v
'''sxal'''
# def password(pasword):
#     count_chars = 0
#     chars = ['!','@','#','$','%','^','&','*','/']
#     while(True):
#         if len(pasword) > 8:
#             for i in pasword:
#                 if i in chars:
#                     count_chars += 1
#         else:
#             print('noric pordzel')
#         if count_chars > 2:
#             print('Passwordy chisht e ')
#             break

# pasword = input('Enter your password --> ')
# password(pasword)


# def calculator(expr):
#     for i in expr:

#         if i == '+':
#             return (expr[::i-1]) + (expr[i+1::])
#         if i == '-':
#             return (expr[::i-1]) - (expr [i+1::])
#         if i == '*':
#             return (expr[::i-1]) * (expr [i+1::])
#         if i == '/':
#             return (expr[::i-1]) / (expr [i+1::])
# # expr = list(input('enter--->'))
# expr = input()
# print(calculator(expr))

# expr = input()
# for i in expr:
#     if i == '+':
#         a = expr[::i-1]
#         a = int(a)
#         b = expr[i+1::]
#         b = int(b)
#         print(a + b)


# with open('file1.txt','w') as file:
#     message1 = input('write message1')
#     file.write(message1)
# f1 = open('file1.txt', 'rt')
# print(f1.read())

# f = open('file1.txt','r')
# for i in range(0,3):
#     print(f.readline())


# f = open('file1.txt','a')
# f.write('hello')

# f = open('file1.txt','rt')
# t = sorted(f,key = len)
# print(t[-1])
    
# kod grel sortavorelu hamar ` ssasaaaakklaaa,aranc sort ogtagortselu

# with open('file2.txt','w') as file:
#     test = input('Enter text ')
#     file.write(test)





# login = input('Enter login ')
# password = input('Enter password ')
# f = open('file2.txt', 'rt')
# res = f.readlines()
# test = 'login-'+login+',password-'+password+'\n'
# for i in res:
#     if i == test:
#         print('True')
#         break
# else:
#     print('False')


# user1 = {
#     'age':20,
#     'profession' : 'programmer'
# }
# file = json.dump('file2.txt')
# file = open('file2.json') 
# data_users = json.load(file)
# users = [user1]
# with open(data_users, 'w') as file:
#     json.dump(users, file)

# import json

# file_name = 'file2.json'

# user = {
#     'name':'knarik',
#     'age':20,
#     'Profession':'Programmer'
# }

# users = [user]
#
#  with open(file_name, 'w') as file:
#     json.dump(users, file)
# file = open('file2.json') 
# data_users = json.load(file)
# print(data_users)

# name = input('Enter name ')
# file = open('file2.json') 
# if name in file:
#     print('yes')
# else:
# #     print('no')
# import json

# my_dict = {}
# first = ['Ani','jessy','ben']
# second = [1,2,3]
# for y,x in zip(second,first):
#     my_dict.setdefault(y,x)
# print(my_dict)

# file_name = 'file2.json'
# with open(file_name, 'a') as file:
#      json.dump(my_dict, file)

# res = []
# number = int(input('enter number '))
# for i in range(2,number):  |
#     for j in range(2,i):  |
#         if i % j != 0:
#             res.append(i)
# print(res)

# import json
# user = {
#     'name':'knarik',
#      'age':20,
# }

# with open('file2.json','a') as file:
#     json.dump(user,file)

#----sharunakell

# list1 = [10,75,43,15,25,-4,27]
# for i in range(0,len(list1)-1):
#     for j in range(0,len(list1)- 1):
#         if list1[j] > list1[j+1]:
            
#             list1[j+1] = list1[j]
#             list1[j] = list1[j+1]
# print(list1) 

# list1 = [1,2,34,56,67,90,98]
# number = int(input('Enter number '))
# mid = len(list1) // 2
# if number > list1[mid]:
#     for i in range(mid,len(list1)):
#         if number == list1[i]:
#             print(i)
# else:
    
#     for i in range(0,mid):
#         if number == list1[i]:
#             print(i)

'''lesson 20'''

# def BinarySearch(list1,number):
#     l = 0
#     r = len(list1)-1
#     while l <= r:
#             mid = (l + r) // 2
#             if list1[mid] == number:
#                 return mid
#             elif(list1[mid] > number):
                
#                 r = mid - 1 
                
#             else:
#                 l = mid + 1 
        
# list1 = [1,3,5,7,8]
# print(BinarySearch(list1,8))



# def BinarySearch(list1,number,start,end):

#         mid = (start + end) // 2
#         if list1[mid] == number:
#             return mid
#         elif(list1[mid] > number):
           
#             return BinarySearch(list1,number,start,mid-1)        
#         else:
            
#             return BinarySearch(list1,number,mid + 1 ,end)
            
# list1 = [1,3,5,7,8]
# start = 0
# end = len(list1)
# print(BinarySearch(list1,8,start,end))


# res = []
# ress = []
# mydict = {'a' : 1,'b' : 2,'c': 2}
# for i in mydict.values():
#     res.append(i)

# ress.append(mydict.keys())
# print(res)
# print(ress)

# for i in res:
#     for j in res:
#         if res[j] == res[j+1]:
#             indx = j

