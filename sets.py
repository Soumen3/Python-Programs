# define set 
s=set()
s.add(1)
s.add(2)
print(s)
s={3,4}
print(s)

s={1,8,2,3}
print('Length of the set is:',len(s))
s.remove(8)
print('After remove 8:',s)
s.pop()
print('After popping:',s)
s.clear()
print('The set is cleared:',s)
s={1,8,2,3}
s.union({8,11})
print(s)
s.intersection({8,11})
print(s)