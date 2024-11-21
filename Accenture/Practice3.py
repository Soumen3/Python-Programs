# You are given a function.
# int CheckPassword(char str[], int n);
# The function accepts string str of size n as an argument. Implement the function which returns 1 if given string str is valid password else 0.
# str is a valid password if it satisfies the below conditions.
# – At least 4 characters
# – At least one numeric digit
# – At Least one Capital Letter
# – Must not have space or slash (/)
# – Starting character must not be a number
# Assumption:
# Input string will not be empty.
# Example:
# Input 1:
# aA1_67
# Input 2:
# a987 abC012
# Output 1:
# 1
# Output 2:
# 0


def CheckPassword(str, n):
    if n < 4:
        return 0
    if str[0].isnumeric():
        return 0
    if ' ' in str or '/' in str:
        return 0
    if not any(char.isdigit() for char in str):
        return 0
    if not any(char.isupper() for char in str):
        return 0
    return 1


password = "aA1_67"
print(CheckPassword(password, len(password)))