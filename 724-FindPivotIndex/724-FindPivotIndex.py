# Last updated: 6/25/2025, 11:43:04 AM
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        totalSum = sum(nums)
        left_sum = 0
        for i in range(len(nums)):
            right_sum = totalSum - nums[i] - left_sum
            if left_sum == right_sum:
                return i
                
            left_sum += nums[i]
        return -1