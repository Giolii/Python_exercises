# Last updated: 6/28/2025, 3:20:04 PM
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        box = {}
        result = 0
        
        for jewel in jewels:
            box[jewel] = 1
        
        for stone in stones:
            if stone in box:
                result+=1
        return result
                
            