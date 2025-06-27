# Last updated: 6/27/2025, 11:53:02 AM
class Solution:
    def firstUniqChar(self, s: str) -> int:
        seen = {}
        for i,char in enumerate(s):
            if char in seen:
                seen[char] = 'x'
            else:
                seen[char] = i
        
        for key in seen:
            if type(seen[key]) == int:
                return seen[key]
        return -1