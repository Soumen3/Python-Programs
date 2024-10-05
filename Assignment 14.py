              # Assignment 14
                          # more on loops

# 1. Write a Python script to create a list of first N natural numbers.
l1=[e for e in range(1,int(input('Enter the value of N:'))+1)]
print(l1)





# 2. Write a Python script to create a list of first N odd natural numbers.
l1=[e*2+1 for e in range(int(input('Enter the value of N:'))+1)]
print(l1)




# 3. Write a Python script to create a list of first N even natural numbers.
l1=[e*2 for e in range(1,int(input('Enter the value of N:'))+1)]
print(l1)





# 4. Write a Python script to find the greatest number in a given list of numbers.
l1=[int(e) for e in input('Enter a list seperated by space:\t').split()]
print('Greatest number of the list is: ',max(l1))





# 5. Write a Python script to find the smallest number in a given list of numbers.

l1=[int(e) for e in input('Enter a list seperated by space:\t').split()]
print('Smallesr number of the list is: ',min(l1))





# 6. Write a Python script to calculate the sum of elements in a given list of numbers.

l1=[eval(e) for e in input('Enter a list of numbers separated by space:\t').split()]
print('The sum of the elements is:',sum(l1))




# 7. Write a Python script to remove all non int values from a list.
lst=['soumen', 32, (21,43), 76, 55.4, 45]
index=0
for i in lst:
    if type(i)!=int:
        del lst[index] 
    index+=1

print(lst)





# 8. Write a Python script to print distinct elements along with their frequencies of occurrence in the list.

lst=[2,4,5,2,6,8,7,6,9,1,5,7,8,5,1,3,6,7,9]
lst2=[]
for e in lst:
    if e not in lst2:
        lst2.append(e)

for i in lst2:
    count=0
    for j in lst:
        if i==j:
            count+=1
    
    print(i,":",count)






# 9. Write a Python script to print indices of all occurrences of a given element in a given list.

lst=[1,2,7,'Soumen','samanta', 'ineuron', 'hello', 45.7, 44]
for i in lst:
    print(f'index of {i} is {lst.index(i)}')




# 10. Write a python script to sort a list.

lst=[int(e) for e in input('Enter the numbers seperated by space:\n').split()]
lst.sort()
print('After sorting the array:\n',lst)



