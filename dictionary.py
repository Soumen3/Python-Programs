# define a dictionary
print('\n               Define a Dictionary')
a={
    'key':'value',
    'Name':'Soumen',
    'Dept.':'BCA',
    'list':[4,3,2,1]
}
print(a)
print(a['Name'])
print('The items are:',a.items())
print('The keys are:',a.keys())
a.update({'friends':'Noone'})
print('The keys are:',a.items())
print(a.get('Name'))