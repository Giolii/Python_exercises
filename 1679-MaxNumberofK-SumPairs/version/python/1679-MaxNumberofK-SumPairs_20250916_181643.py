# Last updated: 9/16/2025, 6:16:43 PM
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        freq = Counter(nums)
        count = 0

        for key in freq:
            if k - key in freq:
                if k - key == key:
                    count += freq[key] // 2
                else:
                    count += min(freq[key],freq[k-key])
                freq[key] = 0
        return count