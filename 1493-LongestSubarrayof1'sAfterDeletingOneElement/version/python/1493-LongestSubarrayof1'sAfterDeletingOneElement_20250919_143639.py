# Last updated: 9/19/2025, 2:36:39 PM
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left, deleted = 0,0

        for right in range(len(nums)):
            if nums[right] == 0:
                deleted += 1
            if deleted > 1:
                if nums[left] == 0:
                    deleted -= 1
                left += 1
        return right - left



        # left,deleted = 0,0

        # for right in range(len(nums)):
        #     if nums[right] == 0:
        #         deleted += 1
        #     if deleted > 1:
        #         if nums[left] == 0:
        #             deleted -= 1
        #         left += 1
        # return right - left