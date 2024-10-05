try:
    str1=input('Enter a string:\n')
    strToInt=int(str1)
    print('the sequence in integer form is:',strToInt)
except ValueError:
    print ("Can't convert this type of data into integer")
except Exception:
    print('Something error')