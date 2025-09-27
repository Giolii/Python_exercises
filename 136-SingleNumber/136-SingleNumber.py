
# Last updated: 6/25/2025, 6:02:50 PM
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
    
        result = 0
        for num in nums:
            result ^= num
        return result
        
