# Last updated: 9/10/2025, 9:44:31 PM
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        freq = {}
        operations = 0

        for num in nums:
            freq[num] = freq.get(num,0) + 1

        for num in freq:
            complement = k - num
            if complement in freq:
                if num == complement:
                    operations += freq[num] // 2
                    freq[num] = 0
                elif complement > num:
                    pairs = min(freq[num],freq[complement])
                    operations += pairs
                    freq[num] = 0
                    freq[complement] = 0

        return operations

