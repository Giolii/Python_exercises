# Last updated: 9/15/2025, 10:36:25 AM
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set('aeiou')
        curr_vow = max_vow = sum(char in vowels for char in s[:k])
        for i in range(k,len(s)):
            curr_vow += (s[i] in vowels) - (s[i-k] in vowels)
            max_vow = max(max_vow,curr_vow)
            if max_vow == k:
                return k
        return max_vow
            
