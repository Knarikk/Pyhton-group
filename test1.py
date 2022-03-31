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
#inch e funkcian, rekursian
