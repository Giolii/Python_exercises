# Last updated: 7/1/2025, 4:22:15 PM
class Solution:
    memo = {1:1,2:2,3:3,4:5}
    def climbStairs(self, n: int) -> int:
        if n in self.memo:
            return self.memo[n]
        else:
            self.memo[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
            
            return self.memo[n]
            
            
            