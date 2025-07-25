# Last updated: 7/22/2025, 2:56:50 PM
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        start = 1
        end = n
        
        while start <= end:
            mid = (start+end) // 2
            result = guess(mid)
            
            if result == 0:
                return mid
            elif result == 1:
                start = mid + 1
            else:
                end =  mid - 1
                