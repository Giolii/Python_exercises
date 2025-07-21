# Last updated: 7/21/2025, 3:19:58 PM
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for point in points:
            dist = point[0] * point[0] + point[1] * point[1]
            heapq.heappush(heap,(-dist,point))
            if len(heap) > k:
                heapq.heappop(heap)
        
        return [point[1] for point in heap ]
        
