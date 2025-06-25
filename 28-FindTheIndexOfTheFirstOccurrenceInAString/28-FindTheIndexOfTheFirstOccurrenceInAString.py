# Last updated: 6/25/2025, 11:43:41 AM
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i + len(needle)] == needle:
                return i
        return -1