# Last updated: 7/30/2025, 8:20:04 PM
class Solution:
    def findMaximumXOR(self, nums):
        max_xor = 0
        mask = 0
        
        for i in range(31, -1, -1):
            mask = mask | (1 << i)
            prefixes = set()
            
            for num in nums:
                prefixes.add(num & mask)
            
            tmp = max_xor | (1 << i)
            
            for prefix in prefixes:
                if (tmp ^ prefix) in prefixes:
                    max_xor = tmp
                    break
        
        return max_xor