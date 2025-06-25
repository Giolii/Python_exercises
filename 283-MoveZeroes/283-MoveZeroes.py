# Last updated: 6/25/2025, 11:43:19 AM
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        notZero = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[notZero] = nums[i]
                notZero += 1
        for j in range(notZero, len(nums)):
            nums[j] = 0
            
        