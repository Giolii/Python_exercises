# Last updated: 6/25/2025, 11:43:38 AM
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)-1,-1,-1):
            digits[i] += 1
            if digits[i] < 10:
                return digits
            digits[i] = 0
        return [1] + digits
        