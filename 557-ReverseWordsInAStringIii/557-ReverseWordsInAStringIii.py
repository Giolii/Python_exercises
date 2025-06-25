# Last updated: 6/25/2025, 11:43:09 AM
class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(' ')
        result = []
        
        for word in words:
            rev_word = word[::-1]
            result.append(rev_word)
        return ' '.join(result)
            
                       
        
            