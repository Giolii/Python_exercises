# Last updated: 7/10/2025, 4:46:47 PM
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        
        stack = []
        brackets = {']':'[',')':'(','}':'{'}
        for char in s:
            if char in brackets:
                if not stack or stack.pop() != brackets[char]:
                    return False
            else:
                stack.append(char)
        return len(stack) == 0