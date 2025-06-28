# Last updated: 6/28/2025, 3:21:12 PM
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        left = 0
        max_length = 0
        
        for right in range(len(s)):
            
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
                
            char_set.add(s[right])
            current_length = right - left + 1
            max_length = max(max_length,current_length)
        return max_length