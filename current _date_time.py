from datetime import datetime
print('Current time is:',datetime.now().strftime("%d-%m-%Y %H:%M:%S"), sep='\n')

# same as above
now = datetime.now()
print ("Current date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))