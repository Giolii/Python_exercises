# Last updated: 7/22/2025, 2:57:39 PM
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            
            if nums[mid] < nums[mid+1]:
                left = mid + 1
            else:
                right = mid
        return left