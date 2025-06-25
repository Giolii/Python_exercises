# Last updated: 6/25/2025, 11:43:12 AM
from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max = 0
        max2 = 0
        for item in nums:
            if(item == 1 ): max2 += 1
            if(item == 0): 
                if(max2 > max):
                    max = max2 
                max2 = 0
        if(max2> max):
            max = max2
        return max