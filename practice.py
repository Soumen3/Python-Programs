# lst=[1,2,3,4,5,6,7]
# print(lst)
# def change(lst):
#     lst[5]=100
#     return lst

# def change2(lst):
#     lst[5]=200
#     return lst

# print(change(lst))
# print(lst)
# print(change2(lst))
# print(lst)









# def set_list(list):
# 	list = ["A", "B", "C"]
# 	return list

# def add(list):
# 	list.append("D")
# 	return list

# my_list = ["E"]

# print(set_list(my_list))

# print(add(my_list))


# s=str()

# print('str is:',len(s))






# class Solution:
    
#     def swap(self,lst,i,j):
#         temp=lst[i]
#         lst[i]=lst[j]
#         lst[j]=temp
    
#     def sort(self, lst):
#         for i in range(len(lst)):
#             for j in range(i+1,len(lst)):
#                 if lst[i]>lst[j]:
#                     self.swap(lst,i,j)
        
    
#     def mergeTwoLists(self, list1, list2) :
        
#         self.sort(list1)
#         self.sort(list2)
        
#         result=[]
#         len1,len2=len(list1),len(list2)
#         i,j=0,0
        
#         while i<len1 and j<len2:
#             if list1[i]<list2[j]:
#                 result.append(list1[i])
#                 i+=1
#             else:
#                 result.append(list2[j])
#                 j+=1
                
#         while i<len1:
#             result.append(list1[i])
#             i+=1
#         while j<len2:
#             result.append(list2[j])
#             j+=1
            
#         return result
    
# obj=Solution()
# list1=[1,3,5,6,8,2]
# list2=[2,4,22,32,11,23]

# print(obj.mergeTwoLists(list1,list2))





# digits=[1,2,4,9]
# res = int("".join([str(i) for i in digits]))
# res+=1
# res=str(res)
# digits=[int(i) for i in res]
# print(digits)





# # paskal's triangle
# import math

# class Solution:
#     def fact(self,n:int):
#         return math.factorial(n)
    
#     def ncr(self,i:int,j:int):
#         return int(self.fact(i)/(self.fact(i-j)*self.fact(j)))  # nCr formula

#     def generate(self, n:int):
#         lst=[]
        
#         for i in range(n):
#             inner=[]
#             for j in range(0,i+1):
#                 inner.append(self.ncr(i,j))
            
#             lst.append(inner)
#             del inner

#         return lst

# obj=Solution()
# print(obj.generate(3))








# # best time to buy and sell

# class Solution:
#     def maxProfit(self, prices) -> int:
#         if len(prices)<=1: return 0
#         profit=0
#         min=prices[0]
#         for i in range(1,len(prices)):
#             if prices[i]<min: min=prices[i] 
            
#             else:
#                 if prices[i]-min>profit:
#                     profit= prices[i]-min
#         return profit
                

# obj=Solution()
# lst=[7,1,5,3,6,4]
# print(obj.maxProfit(lst))





# n=int(input("Enter a number: "))

# if n<0:
#     re=1
    
#     while n<0:
#         re=re*n
#         n+=1
# else:
#     re=1
#     for i in range(1,n+1):
#         re=re*i

# print(re)






# val=input("Enter a vlaue:\t")
# re=val.isnumeric()
# if re== True:
#     print("The value is number")
# else:
#     print("The value is not a number")






# print('as'.upper())

# print(abs(-2.564423))









# class Solution:
#     def containsNearbyDuplicate(self, nums,k) -> bool:
#         # for i in range(len(nums)):
#         #     if nums[i] in nums[i+1:]:
#         #         j=nums[i+1:].index(nums[i])+i+1
#         #         if abs(i - j) <= k:
#         #             return True
#         #         else:
#         #             return False
#         # else:
#         #     return False

#         for i in range(len(nums)):    
#             for j in range(i+1,len(nums)):
#                 if nums[i] is nums[j]:
#                     if abs(i-j) <=k :
#                         return True
   
#         return False
                    


# obj=Solution()
# print(obj.containsNearbyDuplicate([1,0,1,1],1))
# print(obj.containsNearbyDuplicate([1,2,3,1,2,3],2))










# class Solution:
#     def summaryRanges(self, nums) -> list[str]:
#         Ranges=[]
#         i=0
#         while i<len(nums):
#             start=nums[i]
#             while i+1<len(nums) and nums[i+1]==nums[i]+1:
#                 i+=1
#             if start != nums[i]:
#                 Ranges.append(f"{start}-->{nums[i]}")
#             else:
#                 Ranges.append(str(nums[i]))
#             i+=1
#         return Ranges


# obj=Solution()

# nums = [0,1,2,4,5,7]

# print(obj.summaryRanges(nums))







# class Solution:
#     def missingNumber(self, nums) -> int:
#         maxi=len(nums)
#         mini=0

#         for i in range(mini, maxi+1):
#             if i in nums:
#                 continue
#             return i

# obj=Solution()

# nums = [1]

# print(obj.missingNumber(nums))







# string=input("Enter string:")
# sub_str=input("Enter word:")
# if(string.find(sub_str)==-1):
#       print("Substring not found in string!")
# else:
#       print("Substring in string!")

# print(string.find(sub_str))






# string="hello    world          "
# print(len(string.split()))
# print(string.split())



# import math

# x=9.848475
# print(math.floor(x))

# print(round(math.sqrt(5)))












# class Solution:
#     def binaryAdd(self, a , b )->str:
#         carry=0
#         result=''
#         a,b= list(a),list(b)

#         while a or b or carry==1:
#             if a != None:
#                 carry+=int(a.pop())
#             if b != None:
#                 carry+=int(a.pop())

#             result+=str(carry%2)
#             carry= carry//2

#         return result[::-1]

# obj=Solution()
# a='11'
# b='1'
# print(obj.binaryAdd(a,b))



# # get the number only from a string
# import re

# string = 'hello 43 hi 56. soumen 10'
# pattern='\d+'
# result=re.findall(pattern, string)
# print(result)


# # remove white space 
# print(string.replace(' ',''))
# print(string)


# string='hello i am soumen, i am a software engineer'
# pattern='\s+'
# replace=''
# result=re.subn(pattern,replace,string)
# print(result)








# x,y=7,7
# string='prpptppr'
# string2='abppprrr'
# separate=string.split('pr')
# count=separate.count('')
# print(x*count)




import re

#Check if the string starts with "The" and ends with "Spain":

txt = "The rain in Spains"
x = re.search("^The.*Spain$", txt)

if x:
  print("YES! We have a match!")
else:
  print("No match")
