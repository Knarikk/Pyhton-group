'''N1'''

#1-100            return 1
#101 - 999        3 angam baj - > 1
#1000- 9999       4 angam baj - > 2
#10000-99999      5 angam baj - > 3
     
# class Century:
#     def __init__(self,year):
#         self.year = year
#     def century(self):
#         if self.year >= 1 and self.year <= 100:
#             return 1
#         else:
#             if self.year % 100 == 0:
#                 self.year = str(self.year)
#                 m = (self.year)[0:(len(self.year) - 2)]
#                 return int(m)
#             else:
#                 self.year = str(self.year)
#                 m = (self.year)[0:(len(self.year) - 2)]
#                 return int(m)+ 1 

# p = Century(1900)
# print(p.century())



'''N2'''
# class PALindrOme:
#     def __init__(self,word):
#         self.word = word
#     def palindrom(self):
#         if  len(self.word)>=1 and len(self.word)<=105 and self.word[::-1]== self.word:
#             print('Word is Palindrom')
#         else:
#             print('Word is not Palindrom')
# p =  PALindrOme('aba')
# p.palindrom()

'''N3'''
# class LARGesT:
#     def __init__(self,mylist):
#         self.mylist = mylist
#     def maximum(self):
#         res = []
#         for i in range(0,len(self.mylist)-1):
#             mul = self.mylist[i] * self.mylist[i+1]
#             res.append(mul)
#         return max(res)
# mylist = [3, 6, -2, -5, 7, 3]
# p = LARGesT(mylist)
# print(p.maximum())

'''N4 '''

# class LargestWord:
#     def __init__(self,mylist):
#         self.mylist = mylist
#     def func(self):
#         list1 = []
#         j = 0
#         res = sorted(self.mylist,key = len,reverse = True)
#         print(res)
#         list1.append(res[j])
#         for i in range(1,len(res)):
#             if len(res[i]) == len(res[j]):
#                 list1.append(res[i])
#                 j += 1
#         print(list1)
  
# p = LargestWord(["aba", "aa", "ad", "vcd", "aba"])
# p.func()



'''N5'''
# class Lucky:
#     def __init__(self,number,sum1,sum2):
#         self.number = number
#         self.sum1 = sum1
#         self.sum2 = sum2

#     def func(self):
#         self.number = str(self.number)
    
#         length = (len(str(self.number))) // 2
#         for i in range(0,length):
#             self.sum1 += int(self.number[i])
#         for i in range(length,len(str(self.number))):
#             self.sum2 += int(self.number[i])
#         if self.sum1 == self.sum2:
#             print('Number is lucky')
#         else:
#             print('Number is not lucky')
# p = Lucky(10001,0,0)
# p.func()

'''N6'''
# class ListSort:
#     def __init__(self,mylist):
#         self.mylist = mylist
#     def sort(self):
#         j = 0
#         list1 = []
#         for i in range (0,len(self.mylist)):
#             if self.mylist[i] != -1:
#                 list1.append(self.mylist[i])
#         list1.sort()
#         for  i in range(0,len(self.mylist)):
#             if self.mylist[i] != -1:
#                 del self.mylist[i]
#                 self.mylist.insert(i,list1[j])
#                 j += 1
#         print(self.mylist)

# a = [-1, 150, 190, 170, -1, -1, 160, 180]
# p = ListSort(a)
# p.sort()

'''N7'''

# class Weight:
#     def __init__(self,mylist):
#         self.mylist = mylist
#     def func(self):
#         sum1 = 0
#         sum2 = 0
#         for i in range(0,len(self.mylist)):
#             if i % 2 == 0:
#                 sum1 += self.mylist[i]
#             else:
#                 sum2 += self.mylist[i] 
#         return sum1,sum2
# a = [50, 60, 60, 45, 70]
# p = Weight(a)
# print(p.func())
