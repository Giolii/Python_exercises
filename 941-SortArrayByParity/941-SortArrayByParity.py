# Last updated: 6/25/2025, 11:42:58 AM
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        p = 0
        
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                nums[i],nums[p] = nums[p],nums[i]
                p += 1 
        return nums
        