d1={102:'Rahul',103:'Payel',104:'Arjun',105:'Prachi'}
print(d1)
d1[102]='Ravi'
print(d1)
# d1[102]=('Ravi','Dilip')
# print(d1)

print(d1.items())
print(type(d1.items()))

for i in d1.items():
    print(i)

for i,j in d1.items():
    print(i,j)



print(d1.keys())
print(d1.values())

print(len(d1))
print(min(d1))
print(max(d1))
print(sum(d1))

print(d1.pop(102))
print(d1)

print(d1.popitem())
print(d1)
# print(d1.clear())

d2={e:e**2 for e in range(1,6)}
print(d2)



# # user input
# n=int(input('How many student data you want to store:\t'))
# d3={}
# for e in range(n):
#     key=int(input('Enter the roll:\t'))
#     data=input('Enter student name:')
#     d3[key]=data
# print(d3)



# Exercise 1: Convert two lists into a dictionary
value=['one','two','three','four','five','six','seven']
key=[1,2,3,4,5,6,7]
d={}
for i in range(7):
    d[key[i]]=value[i]
print(d)

# or
z=dict(zip(key,value))
print(z)



# Exercise 2: Merge two Python dictionaries into one

dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

dict3={**dict1, **dict2}
print(dict3)

# or
dict3=dict1.copy()
dict3.update(dict2)
print(dict3)

# or
dict1.update(dict2)
print(dict1)



# Exercise 3: Print the value of key ‘history’ from the below dict

sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}

# understand how to located the nested key
# sampleDict['class'] = {'student': {'name': 'Mike', 'marks': {'physics': 70, 'history': 80}}}
# sampleDict['class']['student'] = {'name': 'Mike', 'marks': {'physics': 70, 'history': 80}}
# sampleDict['class']['student']['marks'] = {'physics': 70, 'history': 80}


print(sampleDict['class']['student']['marks']['history'])




# Exercise 4: Initialize dictionary with default values

employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}

dict4={}
for i in range(len(employees)):
    dict4[employees[i]]=defaults
print(dict4)

# or
# The fromkeys() method returns a dictionary with the specified keys and the specified value.
dict4=dict.fromkeys(employees,defaults)
print(dict4)





# Exercise 5: Create a dictionary by extracting the keys from a given dictionary

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

# Keys to extract
keys = ["name", "salary"]

newDict={k:sample_dict[k] for k in keys}
print(newDict)



# Exercise 6: Delete a list of keys from a dictionary

sampl_dict = {
    "name": "soumen",
    "age": 24,
    "salary": 35000000,
    "city": "Kolkata"
}

# Keys to remove
keys = ["age", "city"]

for i in keys:
    sampl_dict.pop(i)
print(sampl_dict)




# Exercise 7: Write a Python program to check if value 200 exists in the following dictionary.

sample_dict = {'a': 100, 'b': 200, 'c': 300}

if 200 in sample_dict.values():
    print('200 is present in the dict')
else: print('200 is not present in the dict')





# Exercise 8: Write a program to rename a key city to a location in the following dictionary.

sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}

del sample_dict['city']
sample_dict['location']='New York'
print(sample_dict)



# Exercise 9: Get the key of a minimum value from the following dictionary
sample_dict = {
  'Physics': 82,
  'Math': 65,
  'history': 75
}

print(min(sample_dict))




# Exercise 9: Write a Python program to change Brad’s salary to 8500 in the following dictionary.

sample_dict = {
    'emp1': {'name': 'Jhon', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 500}
}

sample_dict['emp3']['salary']=8500
print(sample_dict)