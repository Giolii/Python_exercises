# Last updated: 9/8/2025, 1:54:57 PM
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == "":
            return True
        i = 0
        j = 0

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                if i == len(s) - 1:
                    return True
                i += 1
            j += 1
        return False
