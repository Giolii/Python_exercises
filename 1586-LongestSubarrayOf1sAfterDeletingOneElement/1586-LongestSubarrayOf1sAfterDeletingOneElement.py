# Last updated: 9/15/2025, 10:36:24 AM
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        deleted = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                deleted += 1
            if deleted > 1:
                if nums[left] == 0:
                    deleted -= 1
                left += 1
        return right - left


        