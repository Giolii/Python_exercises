# Last updated: 7/21/2025, 3:20:44 PM
class Solution:
    def mySqrt(self, x: int) -> int:
        
        if x < 2:
            return x
        
        start = 0 
        end = x
        
        while start < end:
            mid = (start + end) // 2
            if mid*mid == x:
                return mid
            elif mid*mid < x:
                start = mid + 1
            else:
                end = mid
        return start - 1