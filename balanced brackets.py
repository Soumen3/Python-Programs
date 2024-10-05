class Solution:
    def isValid(self,brk) -> bool:
        stack=[]
        startingBracket=['(','{','[']

        for e in brk:
            if e in startingBracket:
                stack.append(e)
            else:
                if not stack:
                    return False

                currentTop=stack.pop()
                if currentTop=='(':
                    if e != ')':
                        return False
                if currentTop=='{':
                    if e != '}':
                        return False
                if currentTop=='[':
                    if e != ']':
                        return False
                
        if stack:
            return False
        return True


s='()({[]})'
obj=Solution()
print('true') if obj.isValid(s) else print('false')
                
                


