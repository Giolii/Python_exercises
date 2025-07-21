# Last updated: 7/21/2025, 3:19:56 PM
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-stone for stone in stones]
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            heapq.heappush(max_heap,heapq.heappop(max_heap) - heapq.heappop(max_heap))
        return -max_heap[0]