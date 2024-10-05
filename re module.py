import re

# split()          ->  split(pattern,string,maxsplit,flags)
string='I am a programmer'
print(re.split('\s+',string))
print(re.split('\s+',string,2))
print(re.split('\s+',string,2,2))






# sub()             ->   sub(pattern, repl, string, count=0, flags=0)
s1='my ph no is: 9382532340'
print('\nsub() function:\n')
print(re.sub('[0-9]','X',s1))




# subn()
print('\nsubn() function:\n')

print(re.subn('ov', '~*' , 'movie tickets booking in online')) 
t = re.subn('ov', '~*' , 'movie tickets booking in online', flags = re.IGNORECASE) 
print(t) 
print(len(t)) 
print(t[0])
