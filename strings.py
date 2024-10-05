
a = 'Soumen'
print(a)
string1 = 'he '
string2 = "is "
string3 = '''a
                genius'''
print(string1 + string2 + string3)


# accessing character in python
print('\n                       Accessing character in python\n')
string1 = 'Soumen'
print('The initial string is '+string1)
print('The first character of the string is '+string1[0])
print('The last character of the string is '+string1[-1])

# reverseing a string
print('\n                       Reversing a string\n')
print('Reverse of the string is '+string1[::-1])

# Reverse a string by using join and reverse function
string1 = "".join(reversed(string1))
print('Reverse the string by using join and reverse function '+string1)

# String slicing
print('\n                       String slicing\n')
string1 = 'Soumen Samanta'
print('The initial string is '+string1)
print('Slicing character from 3-12:', string1[3:12])
print('Slicing character between 3rd and 2nd last:', string1[3:-2])

# Updation of a character
print('\n                       Updation of a chracter\n')
print('The initial string is '+string1)
list1 = list(string1)
list1[2] = 's'
string1 = ''.join(list1)
print('After updating the 2nd index', string1)
# Another way to update
print('Another way to update')
string1 = 'Soumen Samanta'
string2 = string1[0:2]+"s"+string1[3:]
print('After updating the 2nd index', string2)


# Deletion of a character
print("\n                       Deletion of a character\n")
print('The initial string is '+string1)
# 1st way to delete
string2 = string1[0:4]+string1[5:]
print('After deleting the 4th index:', string2)
# 2nd way to delete
list1 = list(string1)
del list1[5]
string2 = ''.join(list1)
print('After deleting the 4th index using del keyword:', string2)


# Delete entire string
print('\n                       Delete entire entire string\n')
print('The initial string is '+string1)
del string1
print('String deleted successfully........')

# Formatting a string
print('\n                       Formatting a string\n')
# Default order
string1 = '{} {} {} {}'.format('The', 'genius', 'is', 'Soumen')
print('Print the string in default string:')
print(string1)
# Positional formatting
string1 = '{3} {2} {0} {1}'.format('The', 'genius', 'is', 'Soumen')
print('Print the string in positional order:')
print(string1)
# Keyword formatting
string1 = '{a} {b} {c} {d}'.format(b='genius', c='is', a='The', d='Soumen')
print('Print the string in order of keywords:')
print(string1)

# Formatting of integers
print('\n                       Formatting of Integer\n')
string1 = '{0:b}'.format(16)
print('Binary representation of 16 is', string1)
# Formatting of floats
print('\n                       Formatting of Floats\n')
string1 = '{0:e}'.format(165.123456789)
print('Exponent representation of 165.123456789 is', string1)
print(string1)
# Rounding off integers
string1 = '{0:.2f}', format(1/6)
print('One-sixth is:')
print(string1)

# String alignment
print('\n                       String alignment\n')
string1 = "|{:<20}|{:^20}|{:>20}".format('How', 'are', 'you')
print('Left, center and right alignment with formatting:')
print(string1)

# Demonstrate aligning of spaces
string1 = "{0:^16} how can i help you {1:<4}?".format('Soumen', 'now')
print(string1)


# Logical operatioon on strings
print('\n                       Logical operation on string\n')
str1 = ''
str2 = 'S'
# repr is used to print a string along with the  quote
print('str1 and str2:', repr(str1 and str2))
print('str2 and str1:', repr(str2 and str1))
print('str1 or str2:', repr(str1 or str2))
print('str2 or str2:', repr(str2 or str1))
str1 = 'A'
print("\nAfter asigning 'A' in str1:\n")
print('str1 and str2:', repr(str1 and str2))
print('str2 and str1:', repr(str2 and str1))
print('str1 or str2:', repr(str1 or str2))
print('str2 or str1:', repr(str2 or str1))
print('not of str1', (not str1))
str1 = ''
print('not of str1', repr(not str1))


# String formatting using %
print('\n                      String foratting using %\n')
variable = '15'
string = "Vaariable as string= %s " % variable
print(string)
print('Variable as raw data =%r' % variable)
variable = int(variable)
string = "Variable as integer= %d" % variable
print(string)
print('Variable as float= %f' % variable)
print('Variable as octal= %o' % variable)
variable = 's'
print("Variable as character=%c " % variable)

# Split a string
print('\n                     Split a string\n')
line = 'Soumen is a genius'
print(line.split())
print(line.split(' ', 2))
line = 'Soumen-is-a-genius'
print(line.split('-'))
