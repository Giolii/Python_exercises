# Last updated: 6/26/2025, 11:33:34 AM
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map = {}
        map2 = {}
        for i,char in enumerate(s):
            if char in map:
                if map[char] != t[i]:
                    return False
            if t[i] in map2:
                if map2[t[i]] != s[i]:
                    return False
            map[char] = t[i]
            map2[t[i]] = char
        return True
            
            