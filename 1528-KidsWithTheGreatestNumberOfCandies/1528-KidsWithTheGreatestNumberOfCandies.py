# Last updated: 8/13/2025, 5:10:07 PM
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        greatest = max(candies)
        return [candy + extraCandies >= greatest for candy in candies]