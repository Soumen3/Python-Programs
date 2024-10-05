import copy

lst1=[1,2,3,4]
lst2=copy.deepcopy(lst1)

print('the id of lst1 is:',id(lst1), lst1)
print('the id of lst2 is:',id(lst2), lst2)
print()

l1=[1,2,[3,4]]
l2=copy.deepcopy(l1)

print('The list l1 is: ',l1)
print('The list l2 is: ',l2)
print()


# If we copy a nested list using deep copy, if we change one item of the nested list, the corresponding item of the another list will remain unchange 
l1[2][0]=6
print('Now list l1 is:',l1)
print('Now list l2 is:',l2)
