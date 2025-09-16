
# Last updated: 6/25/2025, 11:42:55 AM
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        return sum(h != e for h, e in zip(heights, sorted(heights)))
            
