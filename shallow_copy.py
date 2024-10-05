import copy

lst1=[1,2,3,4]
lst2=lst1       # the both object share the same memory location. If one item changed in a object, another will be change

print('id of lst1:',id(lst1))
print('id of lst2:',id(lst2))
print()


# shallow copy                  this makes an another copy of the copied object.
lst2=lst1.copy()
print('The id if the lst2 is:',id(lst2),'\nThe lst2 is:',lst2)


l1=[[1,2,3],[4,5,6],[7,8,9],5,6,7]
l2=copy.copy(l1)        # same as- l2=l1.copy()

print('the list l2 is:',l2)
print()


# If we copy a nested list using shallow copy, if we change one item of the nested list, the corresponding item of the another list will change 
l1[1][2]=100
l1[4]=10
print('the list l1 is:',l1)
print('the list l2 is:',l2)