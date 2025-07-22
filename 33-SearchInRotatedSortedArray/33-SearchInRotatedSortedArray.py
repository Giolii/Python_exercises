# Last updated: 7/22/2025, 2:57:59 PM
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left,right = 0 , n-1
        
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
                
        start = left
        
        left,right = 0, n-1
        
        while left <= right:
            mid = (left + right) // 2
            real_mid = (mid + start) % n
            
            if nums[real_mid] == target:
                return real_mid
            elif nums[real_mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
        
        
        
#         n = len(nums)
#         left,right = 0, n - 1
        
#         while left < right:
#             mid = (left+right) // 2
#             if nums[mid] > nums[right]:
#                 left = mid + 1
#             else:
#                 right = mid
            
#         start = left
#         left,right = 0, n-1
        
#         while left <= right:
#             mid = (left + right) // 2
#             real_mid = (mid + start) % n
            
#             if nums[real_mid] == target:
#                 return real_mid
#             elif nums[real_mid] < target:
#                 left = mid + 1
#             else:
#                 right = mid - 1
#         return -1
            
        
            
        

        
        
        
        
        
#         while left <= right:
#             mid = (left + right) // 2
            
#             if nums[mid] == target:
#                 return mid
            
#             if nums[left] <= nums[mid]:
#                 if nums[left] <= target < nums[mid]:
#                     right = mid -1
#                 else:
#                     left = mid + 1
#             else:
#                 if nums[right] >= target > nums[mid]:
#                     left = mid + 1
#                 else:
#                     right = mid -1
#         return -1
                