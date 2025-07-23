# Last updated: 7/23/2025, 10:06:49 AM
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left,right = 0, len(letters) - 1
        
        if target >= letters[-1]:
            return letters[0]
        
        while left < right:
            mid = (left + right) // 2
            
            if letters[mid] <= target:
                left = mid + 1
            else:
                right = mid
        return letters[left]
            