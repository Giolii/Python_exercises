# Last updated: 7/23/2025, 10:07:08 AM
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left,right = 1, num
        
        while left < right:
            mid = (left+right) // 2
            if mid*mid < num:
                left = mid + 1
            else:
                right = mid
        return left*left == num