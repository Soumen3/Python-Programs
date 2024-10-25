# Sunder Pichai, who is working at a software company forgot the password of his Linkedin
# Account. But he knows the ASCII values of his password in reverse order. Help him to find the
# password.
# To decode the password, first reverse the string of digits, then successively pick valid values
# from the string and convert them to their ASCII equivalents. Some of the values will have two
# digits, and others three. Use the ranges of valid values when decoding the string of digits.
# Some of the ASCII values are given with their characters:
# The ASCII value of A to Z is 65 to 90.
# The ASCII value of a to z is 97 to 122.
# The ASCII value of space characters is 32.
# Note: The password only has alphabets and blank spaces.
# Given a string , decode the password by following the steps mentioned above.
# ConstraintsÔ
# Ò 1<= |s| <=10^Ë
# Ò s[i] is an ascii character in the range [A-Za-z] or a space character
# Sample Input :
# 796115110113721110141108
# Sample Output :
# PrepInsta

# PrepInsta
# Accenture Placement Prepration
# Online Course
# 100+
# Check Now
# Hours
# 96%
# Got Offer

# Courses Screenshots
# from Courses 200+

# Explanation :
# The reversed string will be 801141011127311011511697, which if analysed
# as ascii will be “PrepInsta”
# Input :
# 670219986
# Output :
# DcxL
# Input :
# 5678911401601
# Output :
# jhwWA
# Input:
# 787968021
# Output:
# xVaW


def find_password(ascii):
    password =[]
    ascii=ascii[::-1]
    i=0
    while i<len(ascii):
        val = ascii[i:i+2]

        if (int(val)>=65 and int(val)<=90) or (int(val)>=97 and int(val)<=99) or val=='32':
            password.append(chr(int(val)))
            i+=2
        else:
            val = ascii[i:i+3]
            password.append(chr(int(val)))
            i+=3

    return str(''.join(password))




print(find_password("796115110113721110141108"))
    