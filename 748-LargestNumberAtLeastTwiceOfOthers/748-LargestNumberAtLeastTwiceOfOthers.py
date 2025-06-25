# Last updated: 6/25/2025, 11:43:03 AM
class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        bigIdx = 0
        for i in range(len(nums)):
            if nums[i] >= nums[bigIdx]:
                bigIdx = i
        for i in range(len(nums)):
            if i != bigIdx and nums[i] * 2 > nums[bigIdx]:
                return -1
        return bigIdx
            
            
            