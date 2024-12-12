# n=int(input())
# arr=[]
# for i in range(n):
#     arr.append(input())

# newSet= set(arr)
# print(newSet.__len__())
# del newSet


# obj={}
# for ele in arr:
#     if ele in obj:
#         obj[ele]+=1
#     else:
#         obj[ele]=1

# for ele in obj.values():
#     print(ele,end=" ")


# List Comprehesion @HackerRank

# x = int(input())
# y = int(input())
# z = int(input())
# n = int(input())

# permutations = [[m,n,o] for m in range(x+1) for n in range(y+1) for o in range(z+1)]
# newPerm=[l for l in permutations if sum(l) != n]
# print((permutations))
# print((newPerm))


# Find the Runner-Up Score! @HackerRank

# n = int(input())
# arr = [int(e) for e in input().split(' ')]
# arr.sort(reverse=True)
# print(arr)

# for i in range(n-1):
#     if (arr[i]>arr[i+1]):
#         print(arr[i+1])
#         break


# Nested List @HackerRank

# students=[]
# for i in range(int(input())):
#     name = input()
#     score = float(input())
#     data=[name, score]
#     students.append(data)

# print(students)

# # sorting the list based on the grade
# students.sort(key=lambda x: x[1])
# print(students)

# second_grade=[]
# smallest_grade=students[0][1]
# highest_grade=students[-1][1]

# for i in range(len(students)):
#     if students[i][1]>smallest_grade and students[i][1] <= highest_grade:
#         second_grade.append(students[i])
#         highest_grade= students[i][1]

# # sorting the lisf of second grade based on the name
# second_grade.sort()
# print(second_grade)
# for student in second_grade:
#     print(student[0])


# sum of multiples of 3 and 5 @ HackerRank

# t = int(input().strip())
# lst_item=[]
# for i in range(t):
#     lst_item.append(int(input().strip()))

# for ele in lst_item:

#     mThree=(ele-1)//3
#     mFive=(ele-1)//5
#     mFifteen=(ele-1)//15

#     result=(3*(mThree*(mThree+1))//2)
#     result += (5*(mFive*(mFive+1))//2)
#     result -= (15*(mFifteen*(mFifteen+1))//2)

#     print(result)


# print("".join(chr(i) for i in range(ord('a'), ord('z')+1)))

# string=['1', '3', '5', '7', '9', 'b', 'd', 'f', 'g', 'j', 'k', 'm', 'n', 'q', 'r', 's', 'u', 'v']
# str(''.join(string))
# print(string)


# Find the percentage @HackerRank

# student_marks = {}
# n = int(input())
# for _ in range(n):
#     name, *line = input().split()
#     scores = list(map(float, line))
#     student_marks[name] = scores
# query_name = input()

# # print(student_marks)
# average=float((sum(student_marks[query_name]))/len(student_marks[query_name]))

# print(format(average, ".2f"))


# Lists @HackerRank

# N = int(input())
# lst=[]
# commands=[]
# for _ in range(N):
#     commands.append(input().split())

# for cmd in commands:
#     if cmd[0]=='insert':
#         lst.insert(int(cmd[1]), int(cmd[2]))
#     elif cmd[0]=='print':
#         print(lst)
#     elif cmd[0]=='remove':
#         lst.remove(int(cmd[1]))
#     elif cmd[0]=='append':
#         lst.append(int(cmd[1]))
#     elif cmd[0]=='sort':
#         lst.sort()
#     elif cmd[0]=='pop':
#         lst.pop()
#     elif cmd[0]=='reverse':
#         lst.reverse()


# subStrings=[]
# string='Soumen'
# for i in range(len(string)-(3-1)):
#     subStrings.append(string[i:i+3])

# print(subStrings)


# def findSubstring(s, k):
#     # Write your code here
#     subStrings=[]
#     for i in range(len(s)-(k-1)):
#         subStrings.append(s[i:i+k])
#     longestVowelString=[]

#     vowels = "aeiouAEIOU"
#     for subString in subStrings:
#         count = sum(subString.count(vowel) for vowel in vowels)
#         if len(longestVowelString)==0:
#             longestVowelString.append(subString)
#             longestVowelString.append(count)
#         elif len(longestVowelString) > 0:
#             if count > longestVowelString[1]:
#                 print(type(longestVowelString[1]))
#                 longestVowelString.pop()
#                 longestVowelString.pop()
#                 longestVowelString.append(subString)
#                 longestVowelString.append(count)

#     if longestVowelString[1]==0:
#         return "Not Found!"
#     return longestVowelString[0]


# print(findSubstring('adiouiuea',5))


# tuples @HackerRank

# n= int(input())
# t=tuple(map(int, input().split()))
# print(hash(t))


# sWAP-cASE @HackerRank

# def swap_case(s):
#     return s.swapcase()

# if __name__ == '__main__':
#     s = input()
#     result = swap_case(s)
#     print(result)


# Find String @HackerRank

# def count_substring(string, sub_string):
#     count=0
#     while(sub_string in string):
#         count+=1
#         string=string[string.index(sub_string)+1:]

#     return count

# if __name__ == '__main__':
#     string = input().strip()
#     sub_string = input().strip()
#     string.index
#     count = count_substring(string, sub_string)
#     print(count)


# String Validation @HackerRank

# if __name__ == '__main__':
#     s = input()

#     # check for any  alphaneumeric character
#     for e in list(s):
#         if e.isalpha() or e.isdigit():
#             print("True")
#             break
#     else:
#         print('False')

#     # check for any alphabet character
#     for e in list(s):
#         if e.isalpha():
#             print("True")
#             break
#     else:
#         print('False')

#     # check for any digit
#     for e in list(s):
#         if e.isdigit():
#             print("True")
#             break
#     else:
#         print('False')

#     # check for any lower case
#     for e in list(s):
#         if e.islower():
#             print("True")
#             break
#     else:
#         print('False')

#     # check for any upper case character
#     for e in list(s):
#         if e.isupper():
#             print("True")
#             break
#     else:
#         print('False')


# #  Text alignment  @HackerRank

# import textwrap

# def wrap(string, max_width):
#     wrapper = textwrap.TextWrapper( width = max_width)
#     word_list=wrapper.wrap(text=string)

#     return '\n'.join(word_list)


# if __name__ == '__main__':
#     string, max_width = input(), int(input())
#     result = wrap(string, max_width)
#     print(result)


# Designer Door Mat @HackerRank

# n, m = map(int, input().split())
# pattern = [('.|.' * (2*i + 1)).center(m, '-') for i in range(n//2)]
# print('\n'.join(pattern + ['WELCOME'.center(m, '-')] + pattern[::-1]))


# String Formating @HackerRank

# n=int(input())
# inSpace=len(bin(n))-1
# for i in range(1,n+1):
#     print(f'{str(i).rjust(inSpace-1)}{oct(i)[2::].rjust(inSpace)}{hex(i)[2::].upper().rjust(inSpace)}{bin(i)[2::].rjust(inSpace)}')


# Alphabet Rangoli @HackerRank

# def print_rangoli(size):
#     n=size
#     alphabets = "abcdefghijklmnopqrstuvwxyz"
#     middleLine=alphabets[n-1::-1]+alphabets[1:n]
#     lengthOfLine=len('-'.join(middleLine))

#     for i in range(1,size+1):
#         print('-'.join(alphabets[n-1:n-i:-1]+alphabets[n-i:n]).center(lengthOfLine, '-'))

#     for i in range(size-1,0,-1):
#         print('-'.join(alphabets[n-1:n-i:-1]+alphabets[n-i:n]).center(lengthOfLine, '-'))


# if __name__ == '__main__':
#     n = int(input())
#     print_rangoli(n)


# Capitalized @HackerRank

# def solve(s:str):
#     string=s.split(' ')
#     print(string)

#     for i in range(len(string)):
#         string[i]=string[i].capitalize()
#     print(string)
#     s= ' '.join(string)
#     return s


# print(solve('hello   world  lol'))


# The Minion Game @HackerRank

# def minion_game(string):
#     vowels='aeiouAEIOU'
#     length=len(string)
#     stuart=0
#     kevin=0

#     for i in range(length):
#         if string[i] in vowels:
#             kevin+=length-i
#         else:
#             stuart+=length-i

#     # print(stuart)
#     # print(kevin)

#     if stuart> kevin:
#         print(f'Stuart {stuart}')
#     elif stuart < kevin:
#         print(f"Kevin {kevin}")
#     else:
#         print("Draw")

# minion_game('Banana')


# Merge the tools @HackerRank

# def merge_the_tools(string, k):
#     # your code goes here
#     # print(type(string))
#     sub_Strings=[string[i:i+k] for i in range(0,len(string),k)]
#     # print(sub_Strings)

#     for i in range(len(sub_Strings)):
#         seen_letters = set()
#         result_string = ""
#         for char in sub_Strings[i]:
#             if char not in seen_letters:
#                 result_string += char
#                 seen_letters.add(char)

#         sub_Strings[i]=result_string

#     for sub_String in sub_Strings:
#         print(sub_String)


# if __name__ == '__main__':
#     string, k ="AABCDABCA", int(3)
#     merge_the_tools(string, k)


# collections.Counter  @HackerRank

# # Enter your code here. Read input from STDIN. Print output to STDOUT

# number_of_shies=int(input())
# sizes=[int(e) for e in input().split(' ')]
# number_of_customers=int(input())
# size_and_price=[]
# for i in range(number_of_customers):
#     items=tuple(int(e) for e in input().split(' '))
#     print(type(items))
#     size_and_price.append(items)

# print(size_and_price)


# def product_of_digits(N, numbers):
#     number = [e for e in numbers if e !=' ']
#     product = 1
#     for num in number:
#         temp=int(num)
#         product *= temp
#     print(product)


# def check_number(n):
#     while n % 2 == 0:
#         n /= 2
#     while n % 3 == 0:
#         n /= 3
#     while n % 5 == 0:
#         n /= 5
#     return n == 1

# def print_numbers():
#     N = int(input())
#     numbers = list(map(int, input().split()))
#     for num in numbers:
#         if check_number(num):
#             print(num, end=' ')
#     print()

# print_numbers()





# The Elixir of Power @HackerRank

# def find_convergence_level(T, test_cases):
#     for i in range(T):
#         N = test_cases[i][0]
#         A = test_cases[i][1]
#         max_sum = 0
#         for j in range(N//2):
#             max_sum = max(max_sum, A[j] + A[N-j-1])
#         print(max_sum)

# # Sample Input
# T = 2
# test_cases = [
#     (5, [24, 87, 45, 62, 3]),
#     (4, [23, 5, 12, 0])
# ]

# find_convergence_level(T, test_cases)


# def find_convergence_level():
#     result=[]
#     T = int(input().strip())
#     for _ in range(T):
#         N = int(input().strip())
#         A = list(map(int, input().strip().split()))
#         max_sum = 0
#         for j in range(N//2):
#             max_sum = max(max_sum, A[j] + A[N-j-1])
#         result.append(max_sum)
#     for i in result:
#         print(i)

# # Call the function
# find_convergence_level()




# Ashwin's Coin Challenge @HackerRank

# def max_withdrawals(X, Y, N):
#     extra_coins = N // 50
#     total_coins = X + extra_coins
#     withdrawals = total_coins // Y
#     if total_coins % Y != 0:
#         withdrawals += 1
#     return withdrawals

# # Sample Input
# X,Y,N=map(int, list((input().split())))

# print(max_withdrawals(X, Y, N))






# # MegaZord Concert: Rock Out Before Rita Repulsa Reigns!  @HackerRank
# def latest_arrival_time():
#     T = int(input())
#     for _ in range(T):
#         N, M, C = map(int, input().split())
#         P = list(map(int, input().split()))
#         F = list(map(int, input().split()))
#         P.sort()
#         F.sort(reverse=True)
#         i = 0
#         j = 0
#         while i < N and j < M:
#             if F[i] > P[j]:
#                 i += 1
#                 j += C
#             else:
#                 j += 1
#         print(F[i-1])

# latest_arrival_time()



# Lily's Homework @HackerRank
# def lilysHomework(arr):
#   """
#   This function finds the minimum number of swaps required to make the array beautiful.

#   Args:
#       arr: A list of distinct integers.

#   Returns:
#       The minimum number of swaps required.
#   """
#   n = len(arr)

#   # Create a copy of the array and sort it
#   sorted_arr = sorted(arr)

#   # Initialize a visited array to track swapped elements
#   visited = [False] * n

#   swaps = 0
#   for i in range(n):
#     # Skip if element is already in its correct position or visited
#     if arr[i] == sorted_arr[i] or visited[i]:
#       continue

#     # Find the index of the element that should be at the current position
#     j = arr.index(sorted_arr[i])

#     # If element is not visited, swap and update visited
#     # if not visited[j]:
#     arr[i], arr[j] = arr[j], arr[i]
#     visited[i] = True
#     visited[j] = True
#     swaps += 1

#   return swaps

# # Example usage
# arr = [2, 5, 3, 1]
# min_swaps = lilysHomework(arr)
# print(f"Minimum swaps required: {min_swaps}")





# Game of thrones - I @HackerRank
# from collections import Counter

# def gameOfThrones(s):
#   """
#   This function checks if a string can be rearranged into a palindrome.

#   Args:
#       s: A string to analyze.

#   Returns:
#       "YES" if the string can be rearranged into a palindrome, "NO" otherwise.
#   """
#   # Count the frequency of each character
#   char_count = Counter(s)
#   print(char_count)

#   # Check if at most one character has an odd frequency
#   odd_count = 0
#   for count in char_count.values():
#     odd_count += count % 2

#   # If there are more than one character with odd frequency, it's not a palindrome
#   return "YES" if odd_count <= 1 else "NO"

# # Example usage
# s = "aabbccdd"
# result = gameOfThrones(s)
# print(result)






# def power(val):
# 	return val**2

# val=4
# print(power(val))
# print(val)


# lst = [10,-4,-30,60, 30, 88, 12, 76, -56]
# lst.sort(reverse=True)
# print(lst)


# class Example:
#     count = 0  # Class variable

# # Create instances of the class
# obj1 = Example()
# obj2 = Example()

# # Access the class variable
# print(Example.count)  # Output: 0
# print(obj1.count)     # Output: 0
# print(obj2.count)     # Output: 0

# # Modify the class variable
# Example.count += 1

# # Access the class variable again
# print(Example.count)  # Output: 1
# print(obj1.count)     # Output: 1
# print(obj2.count)     # Output: 1

# # Modify the class variable through an instance
# obj1.count += 1

# # Access the class variable again
# print(Example.count)  # Output: 1
# print(obj1.count)     # Output: 2
# print(obj2.count)     # Output: 1






# class Parent:
#     def __init__(self, name):
#         self.name = name

#     def display(self):
#         print(f"Parent Name: {self.name}")

# class Child(Parent):
#     def __init__(self, name, age):
#         super().__init__(name)  # Call the __init__ method of the Parent class
#         self.age = age

#     def display(self):
#         super().display()  # Call the display method of the Parent class
#         print(f"Child Age: {self.age}")

# # Create an instance of the Child class
# child = Child("John", 12)

# # Call the display method of the Child class
# child.display()



# def square(x):
#     return x ** 2

# numbers = [1, 2, 3, 4, 5]
# squared_numbers = map(square, numbers)

# # Convert the map object to a list to see the results
# print(type(squared_numbers))
# print(list(squared_numbers))






# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     # overloading the '+' operator
#     def __add__(self, other):
#         x_sum = self.x + other.x
#         y_sum = self.y + other.y
#         return Point(x_sum, y_sum)
    
#     def __str__(self):
#         return f"({self.x}, {self.y})"


# p1 = Point(2, 3)
# p2 = Point(4, 5)
# print(p1)  # Output: (2, 3)
# print(p1+p2)  # Output: (6, 8)










# class Solution:
#     steps=[1,2]


#     def ways(self, n):
#         if n<len(self.steps):
#             return self.steps[n-1]
        
#         self.steps.append(self.ways(n-1)+self.ways(n-2))
#         return self.steps[n-1]

#     def climbStairs(self, n: int) -> int:
#         return self.ways(n)







# lst=[2]
# def name(n):
#     if n<=0:
#         return
#     print("Soumen Samanta",lst)
#     name(n-1)

# name(5)






# def Solution(string):
#     # Write your code here
#     char={}
#     length=0
#     temp=0
#     for i in range(len(string)):
#       if string[i] not in char:
#         char[string[i]]=True
#         temp+=1
#       else:
#         char.clear()
#         if length<temp:
#           length = temp
#         temp=0
#     return length
        
# print(Solution('abcabcbb'))






# def fiboGenerator(num):
#     first=0
#     second=1
#     while num:
#         yield first
#         first, second = second, first+second
#         num-=1
#     return

# print(fiboGenerator(10))





# class Test:
#     def __init__(self):
#         self.a=5
    
#     def f1(self):
#         self.b=10

# t1=Test()
# t2=Test()
# t1.f1()
# t1.c=15

# print(t1.__dict__)
# print(t2.__dict__)






# add = lambda a,b: a+b
# print(add(20,50))





# factorial = lambda n: 1 if n==0 else n* factorial(n-1)
# print(factorial(5))





# expo=lambda a:a**a

# lst=[expo(e) for e in range(1, 11)]
# print(lst)


# list1=[23,45,66,11,48,70,25,84,90,35]
# lst=[e for e in list1 if e%2==0 ]
# print(lst)






# x=5
# def f1():
#     x=4
#     d=globals()
#     print(d['x'],x)
# f1()
# print(x)







# def decor_result(result_function):
#     def distinction(marks):
#         for i in marks:
#             if i>=75:
#                 print("Distinction")
#                 break
#         result_function(marks)
#     return distinction

# @decor_result
# def result(marks):
#     for i in marks:
#         if i >= 35:
#             pass
#         else:
#             print('Fail')
#             break
#     else:
#         print('Pass')

# marks=[45,56,78,90,65,87]
# result(marks)





# def f1():
#     print("First function")

# def f1(a,b):
#     print("Socond function")

# f1()