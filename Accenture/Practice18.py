# Ques: The program is supposed to calculate the sum of  distance between three points from each other.
# For
# x1 = 1 y1 = 1
# x2 = 2 y2 = 4
# x3 = 3 y3 = 6
# Distance is calculated as : sqrt(x2-x1)2 + (y2-y1)2

import math
def findDistance(x1,y1,x2,y2,x3,y3):
    a = math.sqrt(((x2-x1)**2) + ((y2-y1)**2))
    b = math.sqrt(((x3-x2)**2) + ((y3-y2)**2))
    c = math.sqrt(((x3-x1)**2) + ((y3-y1)**2))

    return a+b+c

print(findDistance(1,1,2,4,3,6))
    