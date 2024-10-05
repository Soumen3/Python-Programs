# creating a List
List = []
print('Blank List',)
print(List)
# creating a List of numbers
List = [10,20,30]
print('List of numbers:',List)
# creating a List of string and accessing using index number 
List=['hello', 'boss!','how', 'can','I','help','you?']
print('The List is:',List)
print('List items:')
print(List[0])
print(List[4])


# creating a List with mixed type of values 
print('                 Creating a list with mixed type of value')

List=[1,2,3,'Soumen','samanta',True]
print('List with the mixed type of values')
print(List)


# Accessing elements from a multi-dimentional List 
print('                 Accessing elements from a multi dimensional list')

List=[['how','are','you'],['how', 'can','I','help','you']]
print('Accessing a elements from a multi-dimentional List')
print([List[0][2]])
print([List[1][1]])

# negative indexing
print('                 Negative indexing')

List=[1,2,'soumen','sammanta',4]
print('accessing elements using negative indexing')
print(List[-1])
print(List[-3])


# getting the size of python List
print('                 Getting the size of Python list')

List=[]
print(len(List)) 
List=[1,2,3,45,]
print(len(List)) 


# getting as input in a List from the user 

print('                 Getting as input in a list from the user')

List=[]
n=int(input('Enter the number of elements:'))
print ('Enter the elements:')
for i in range(0,n):
    ele=int(input())
    List.append(ele)
print(List)

# input with handling exception 

print('                 Input with handling exception')
try:
    my_list=[]
    print('Enter the elements:')
    while True:
        my_list.append(int(input()))
except:
    print(my_list)



# input using map 

print('                 Input using map')

n= int(input('Enter the number of elements:'))
a=list(map(int, input('Enter the number:').strip().split()))[:n]
print('List is-',a)



# List of list as input 

print('                 List of list as input')
lst=[]
n=int(input('Enter the number of elements:'))
for i in range(0,n):
    ele=[input(), int(input())]
    lst.append(ele)
print(lst)


# input using list comprehension and typecasting

print('                 Input using list comprehension and typecasting')
lst1=[]
lst2=[]
lst3=[]
lst1=[int(item) for item in input("Enter the list item:").split()]
lst2=[item for item in input("Enter the list item:").split()]
lst3=list(input("Enter the list item:").split())            #same as above

print(lst1)
print(lst2)
print(lst3)



# Adding element to python
print('                 Adding elements to the list')
List=[]
print('The initial list:',List)
# addition of elements in the list using append() method
List.append(1)
List.append(2)
List.append(4)
print('List after adding three elements:',List)
# Adding elements to the list using iterator 
for i in range(5,9):
    List.append(i)
print('List after adding elements 5 to 8',List)
# Adding tuples to the list 
List.append((9,10))
print('List after adding a tuple:',List)
# Addision of list of list 
list2=['Soumen', 'Samanta']
List.append(list2)
print('List after addison of a list of list',List)
# Addition of elements in the list using insert() method 
List=[1,2,3,4]
print('Initial list:',List)
# Adding of elements at specific position 
List.insert(3,12)
List.insert(0,'Soumen')
print('List after performing insert operation:',List)
# Adding multiple elements to the end of the list using extend() keyword
List.extend([1,'Soumen','Samanta'])
print('list after performing extend operation:',List)



# Reversing a list 
print('                 Reversing a list')
mylist=[1,2,3,4,5,6,'Samanta','Soumen']
mylist.reverse()
print('The reverse list is:',mylist)



# Removing elements from the list 
print('                 Removing elements from the list')
List=[1,2,3,4,5,6,7,8,9,10,11,12,13]
# Removing Elements using remove() method 
print('Initial list:',List)
List.remove(4)
List.remove(6)
print('List after removing the two elements:',List)
# Removing elements using pop() method 
List=[1,2,3,4,5,6,7,8,9,10,11,12,13]
List.pop()
print('List after popping the element',List)
List.pop(5)
print('List after popping the spefic element',List)
