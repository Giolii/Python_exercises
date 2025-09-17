# Last updated: 9/16/2025, 5:33:00 PM
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


        