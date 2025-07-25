# Last updated: 7/23/2025, 10:08:19 AM
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left,right = 0, len(nums) - 1
        start = -1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                start = mid
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        left,right = 0, len(nums) - 1
        end = -1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                end = mid
                left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return [start,end]
            
                
