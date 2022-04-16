'''N1'''

# def func(a,b,step):
#     res =[]
#     res.append(a)
#     while a <= b:
#         a += step
#         if a <= b:
#             res.append(a)
#     print(res)
# func(10,100,20)

'''N2'''

# def func(mylist):
#     res = []
#     for i in range(1,len(mylist)):
#         temp = mylist[i] * mylist[i-1]
#         res.append(temp)
#     print(res)

# mylist = [1, 1, 4, 32, 6] 
# func(mylist)

'''N3  wrong!!!!'''
# j = 0
# new_string = ''
# string =  '_, we have a _.'
# mylist = ['Ashot', 'problem',]
# for i in range(0,len(string)):
#     if string[i] == '_':
#         new_string += mylist[j]
#         j+=1
#     else:

#         new_string += string[i]    

# print(new_string)



'''N4'''
# def func(list1):
#     res = []
#     for i in list1:
#         res.append(len(i))
#     return max(res) + min(res)

# list1 = ['anymore', 'raven', 'me', 'communicate'] 
# print(func(list1))


'''N5'''
# def findIndex(mylist,n):
#     res = []
#     for i in range(0,len(mylist)):
#         if mylist[i] == n:
#             return i
#         else:
#             for i in range(0,len(mylist)):
#                 for j in range(1,len(mylist)):
#                     res.append(mylist[i] - mylist[j])
#     print(res)
# mylist = [45,12,48,23,12,23]
# print(findIndex(mylist,15))

'''N6'''
# def func(n):
#     list1 = []
#     list2 = []
#     mydict = {}
#     for i in range(1,n+1):
#         list1.append(i)
#         list2.append(i ** 2)
#     for x,y in zip(list1,list2):
#         mydict.setdefault(x,y)
#     return mydict
# print(func(5))

'''N7'''



'''N8'''
'''without recursion'''
# def fib(n):
#     res = []        
#     n1 = 0
#     n2 = 1
#     res.append(n1)
#     res.append(n2)
#     for i in range(2,n):
#         temp = n1+ n2
#         n1 = n2
#         n2 = temp
#         res.append(n2)
#     return res
# print(fib(9))

'''fib Recursion'''
# def fib(n):
#     if n == 1:
#         return 1
#     elif n == 0:
#         return 0
#     else:
#         return (fib(n-1)) + (fib(n-2))
# print(fib(5))