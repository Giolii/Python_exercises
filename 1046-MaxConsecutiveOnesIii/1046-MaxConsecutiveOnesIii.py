# Last updated: 9/15/2025, 10:36:31 AM
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        i = 0
        for j in range(len(nums)):
            if nums[j] == 0:
                k -= 1
            if k < 0:
                if nums[i] == 0:
                    k += 1
                i += 1
        return j-i+1




        # left,zero_count,max_length = 0,0,0
        # for right in range(len(nums)):
        #     if nums[right] == 0:
        #         zero_count += 1
        #     if zero_count > k:
        #         if nums[left] == 0:
        #             zero_count -= 1
        #         left += 1
        # return right-left + 1





