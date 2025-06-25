# Last updated: 6/25/2025, 11:43:29 AM
class Solution:
    def reverseWords(self, s: str) -> str:
        words = []
        word = ''
        
        for char in s:
            if char != " ":
                word += char
            else:
                if word:
                    words.append(word)
                    word = ''
        if word:
            words.append(word)
            
        reversed = []
        
        for i in range(len(words) -1, -1, -1 ):
            reversed.append(words[i])
            
        result = reversed[0]
        
        for i in range(1, len(reversed)):
            result += ' ' + reversed[i]
        
        return result
            