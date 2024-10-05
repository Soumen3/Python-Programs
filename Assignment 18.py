          # Assignment 18
          #              Dictionary


# 1. Write a python program to create and print a dictionary which stores your information. (name, age, gender …...)

d={'name':'Soumen',
    "age":20,
    "gender":"male",
    "studies":"BCA"
}
print(d)




# 2. Write a python program to access the items of a dictionary by referring to its key name.


d={'name':'Soumen',
    "age":20,
    "gender":"male",
    "studies":"BCA"
}
print(d["name"])
print(d["age"])
print(d["gender"])
print(d["studies"])





# 3. Write a python program to get a list of the values from a dictionary.

d={'name':'Soumen',
    "age":20,
    "gender":"male",
    "studies":"BCA"
}
print(d.values())





# 4. Write a python program to change the value of a specific item by referring to its key name.

d={'name':'Soumen',
    "age":20,
    "gender":"male",
    "studies":"BCA"
}
d["age"]=23
print(d)





# 5. Write a python program to print all key names in the dictionary, one by one.

d={'name':'Soumen',
    "age":20,
    "gender":"male",
    "studies":"BCA"
}
for i in d:
    print(i,end=', ')




# 6. Write a python program to create a dictionary that contains three dictionaries. (nested)

details={
    "Personal":{
        'name':'Soumen',
        "age":20,
        "gender":"male"
        },
    'Education':{
        'school':'Andichak High School(H.S)',
        'college':'Panskura Banamali college (Autonomous)'
    },
    'Address':{
        'vill':'Hajichak',
        'p.s':'Keshpur',
        'dist':'Paschim Medinipur'
    }
}

print(details)






# 7. Write a python program to create three dictionaries, then create one dictionary that will contain the other three dictionaries.

Personal={
        'name':'Soumen',
        "age":20,
        "gender":"male"
        }
Education={
        'school':'Andichak High School(H.S)',
        'college':'Panskura Banamali college (Autonomous)'
    }
Address={
        'vill':'Hajichak',
        'p.s':'Keshpur',
        'dist':'Paschim Medinipur'
    }

details={
    'data1':Personal,
    'data2':Education,
    'data3':Address
    }
print(details)






# 8. Write a python program to convert two lists into a dictionary in a way that item from list1 is the key and item from list2 is the value.

list1=['name', 'age', 'sex']
list2=['soumen', 20, 'male']

dic1={}
for i in range(len(list1)):
    dic1[list1[i]]=list2[i]
print(dic1)






# 9. Write a python program to merge two python dictionaries into one dictionary.

Personal={
    'name':'Soumen',
    "age":20,
    "gender":"male"
    }

Address={
    'vill':'Hajichak',
    'p.s':'Keshpur',
    'dist':'Paschim Medinipur'
    }

Personal.update(Address)
print(Personal)

# Another way

details={**Personal, **Address}

print(details)






# 10. Write a python program to get the key of lowest value from the dictionary.
# sample_dict = {
# 'C': 92,
# 'Java': 66,
# 'Python': 85
# }

sample_dict = {
    'C': 92,
    'Java': 66,
    'Python': 85
}
print(min(sample_dict.values()))



