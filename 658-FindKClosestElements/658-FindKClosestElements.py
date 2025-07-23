# Last updated: 7/23/2025, 10:06:50 AM
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left,right = 0, len(arr) - k
        
        while left < right:
            mid = (left+right) // 2
            if x - arr[mid] > arr[mid+k] - x:
                left = mid + 1
            else:
                right = mid
        return arr[left:left+k]