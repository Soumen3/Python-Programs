# Salman Khan is making a website, in which there is a tab to create a password. As other
# websites, there are rules so that the password gets complex due to which it becomes
# unpredictable for anyone. So he gave some rules like:
# - At least one numeric digit
# - At Least one Small/Lowercase Letter
# - At Least one Capital/Uppercase Letter
# - Must not have space
# - Must not have slash (/)
# - At least 6 characters
# If someone inputs an invalid password, the code prints: "Invalid password".
# Otherwise, it prints: "password valid".
# Input Format:
# A line with a given string as a password
# Output Format:
# If someone inputs an invalid password, the code prints: "Invalid password".
# Otherwise, it prints: "password valid", without the quotation marks.
# Constraints:
# Number of character in the given string <=10^9
# Sample input 1:
# abjnlL09
# Sample output 1:
# password valid
# Sample input 2:
# jjnaskpk
# Sample output 2:
# Invalid password
# Input :
# 2Ab/a6uY


def is_valid_pass(password):
    if len(password) < 6:
        return "Invalid password"
    has_digit = any(char.isdigit() for char in password)
    has_lower = any(char.islower() for char in password)
    has_upper = any(char.isupper() for char in password)
    has_space = ' ' in password
    has_slash = '/' in password
    if has_digit and has_lower and has_upper and not has_space and not has_slash:
        return "password valid"
    else:
        return "Invalid password"

print(is_valid_pass('2fgAgs/'))
