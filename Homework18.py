'''N1'''
# import json
# user = {
#     'name':'knarik',
#      'age':20,
# }

# with open('file2.json','a') as file:
#     json.dump(user,file)

'''N2'''

# import json
# file = open('file2.json') 
# data_users = json.load(file)
# for  i in  data_users:
#     for j in i:
#         print(i)
    

'''N3'''
# import json
# name =input('Enter name ')
# string = 'knarik','olivia','nohan'
# with open('file2.json','w') as file:
#     json.dump(string,file)
# if name in string:
#     print(' yes')
# else:
#     print('no')

'''Exercises '''

'''N1'''

# import json
# mydict = {}
# first = ['Ani', 'Jessy ', 'Ben']  
# second = [1,2,3]
# for x,y in zip(second,first):
#     mydict.setdefault(x,y)
# print(mydict)
# with open('file2.json','a') as file:
#     json.dump(mydict,file)

'''N2'''

# import json
# lyrics = 'Talking to the moon , \
# Trying to get to you , \
# In hopes you''re on the other side talking to me too , \
# Or am I a fool who sits alone talking to the moon '
# with open('song.json','w') as file:
#     json.dump(lyrics,file)
# file = open('song.json')
# song = json.load(file)
# print(song)


'''N3'''

# import json
# number = int(input())
# sum = 0
# for i in  range(1,number):
#     if i % 3 == 0 or i % 5 == 0:
#         sum += i
# with open('file2.json','a') as file:
#     json.dump(sum,file)


'''Parz tveri artadryaly 2-n mijakayqi '''
# import json
# number = int(input())
# mul = 1
# for  i in range(2,number):
    
#         for j in range(2,i):
#             if i % j == 0:
#                 break
#         else:
#                 mul *= i
# print(mul)
# with open('file2.json','a') as file:
#     json.dump(mul,file)

'''N4'''

# import json
# count_vowels = 0
# alpha = 'a','e','i','o','u','y'
# string = input('Enter string ')
# for i in string:
#     if i in alpha:
#         count_vowels += 1
# print(count_vowels)
# with open('file2.json','a') as file:
#     json.dump(count_vowels,file)

'''N5'''

# str = ''
# count_result = []
# mydict={}
# string = 'Another pause and more eying and siding around each other'
# res = string.split(' ') 
# for i in res:
#     count_res = res.count(i)
#     count_result.append(count_res)
# for x,y in zip(res,count_result):
#     mydict.setdefault(x,y)
# print(mydict)


'''N6'''
# import json
# my_list1 = ['a','b','a','c','b']
# mylist2 = []
# for i in my_list1:
#     if i not in mylist2:
#         mylist2.append(i) 
# with open('file2.json','a') as file:
#     json.dump(mylist2,file)
# print(mylist2)

'''N7'''

# import json
# count_upper = 0
# count_lower = 0
# story = 'KKKSJDoofdrfd    okk'
# with open('word.txt','w') as file:
#     json.dump(story,file)
# for i in story:
#     if i.isupper():
#         count_upper += 1
#     elif i.islower():
#         count_lower += 1
# print(count_lower)
# print(count_upper)


