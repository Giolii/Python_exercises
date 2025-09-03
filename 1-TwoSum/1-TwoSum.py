
# Last updated: 6/26/2025, 11:34:22 AM
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        
        for i,val in enumerate(nums):
            m = target - val
            if m in map:
                return [i,map[m]]
            map[val] = i
        return []
            
