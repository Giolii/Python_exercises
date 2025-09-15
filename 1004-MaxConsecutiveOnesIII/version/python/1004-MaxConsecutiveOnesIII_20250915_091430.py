# Last updated: 9/15/2025, 9:14:30 AM
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0

        for right in range(len(nums)):
            if nums[right] ==0:
                k -= 1

            if k < 0:
                if nums[left] == 0:
                    k += 1    
                left += 1

        return right - left + 1