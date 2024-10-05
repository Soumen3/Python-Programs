# A palindrome reads the same from left to right, mom for example. There is a palindrome which must be modified if possible.
# Change Exactly one character of the string to another character in the range of a-z. so that the string meets the following 
# conditions:
# 1. The new string is lower alphabetically than the initial string.
# 2. The new string is lowest value string alphabetically that can be created from the original palindrome after making only one change.
# 3. The new string is not a palindrome.
# Return the new string, or if it not possible to create a string meeting the criteria, return the string IMPOSSIBLE

def new_string(string):
    if len(string) <= 1:
        return "IMPOSSIBLE"
    
    for i in range(len(string)):
        if string[i] != 'a':
            new_str = string[:i] + 'a' + string[i+1:]
            return new_str
    return 'IMPOSSIBLE'

print(new_string('aaa'))