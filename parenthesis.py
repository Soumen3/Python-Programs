# Given a string consist of left and right parentheses, '(' and ')', balance the 
# parentheses by inserting parentheses as necessary. Determine the miimum number of characters must be inserted
# Ex:
# 1. s='(()))'
# insert one left parenthesis at the left of the strong to get "((()))". the string is balances after 1 insertion.

# 2. s='))(('
# insert 2 left parentheses at the start and 2 right parentheses at the end of the string to get (())(()) prime after 4 insertions.

def balance(string):
    opening=0
    closing=0
    for i in string:
        if i == '(':
            opening+=1
        else:
            if opening > 0:
                opening -=1
            else:
                closing+=1
    
    if opening:
        string = string + (')'*opening)
    if closing:
        string = ('('*closing) +string
    
    return string
    


s='))()(()'
bal_str=balance(s)
print(bal_str)
