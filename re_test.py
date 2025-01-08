import re
class Solution:
    def isPrefixOfWord(self, sentence, searchWord):
        # words=sentence.split(' ')
        matches = re.match(r'/se', sentence)
        return matches


obj= Solution()
sentence="i love eating burger"
searchWord="burg"
print(obj.isPrefixOfWord(sentence,searchWord))
