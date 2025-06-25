# Last updated: 6/25/2025, 11:42:52 AM
import math
class Solution:
    def findNumbers(self, nums: List[int]) -> int:  
        evenDigits = 0
    
        for num in nums:
            digits = math.floor(math.log10(num) +1)
            if(digits % 2 == 0): 
                evenDigits += 1
        return evenDigits
                
            
            