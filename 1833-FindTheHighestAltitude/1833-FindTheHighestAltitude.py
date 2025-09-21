# Last updated: 9/21/2025, 10:39:23 AM
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        highest,curr = 0,0
        for num in gain:
            curr += num
            highest = max(curr,highest)
        return highest


        