# Last updated: 7/21/2025, 3:20:29 PM
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heappush(heap,num)
            if len(heap) > k:
                heappop(heap)

        return heap[0]
        