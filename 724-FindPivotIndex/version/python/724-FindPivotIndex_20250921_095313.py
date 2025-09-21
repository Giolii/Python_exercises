# Last updated: 9/21/2025, 9:53:13 AM
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        left_sum = 0
        for i in range(len(nums)):
            right_sum = total_sum - nums[i] - left_sum
            if left_sum == right_sum:
                return i
            left_sum += nums[i]
        return -1
        
        # totalSum = sum(nums)
        # left_sum = 0
        # for i in range(len(nums)):
        #     right_sum = totalSum - nums[i] - left_sum
        #     if left_sum == right_sum:
        #         return i  
        #     left_sum += nums[i]
        # return -1