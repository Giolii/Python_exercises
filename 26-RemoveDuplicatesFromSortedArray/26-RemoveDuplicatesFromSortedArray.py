# Last updated: 6/25/2025, 11:43:43 AM
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        unique = 0
        
        for i in range(1, len(nums)):
            if nums[i] != nums[unique]:
                unique += 1
                nums[unique] = nums[i]
        return unique + 1
            
        