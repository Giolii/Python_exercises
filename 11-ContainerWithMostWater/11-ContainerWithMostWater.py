# Last updated: 9/21/2025, 12:24:31 PM
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1 
        max_area = 0

        while left < right:
            actual_area = min(height[left], height[right]) * (right - left)
            max_area=max(max_area, actual_area)
            if height[left] < height[right]:
                left+=1
            else:
                right-=1
        return max_area
        

