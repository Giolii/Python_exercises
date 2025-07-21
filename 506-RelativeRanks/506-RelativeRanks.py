# Last updated: 7/21/2025, 3:20:15 PM
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n = len(score)
        heap = []

        for index,score in enumerate(score):
            heapq.heappush(heap,(-score,index))
        
        result = [''] * n
        place = 1

        while heap:
            index = heapq.heappop(heap)[1]
            if place == 1:
                result[index] = "Gold Medal"
            elif place == 2:
                result[index] = "Silver Medal"
            elif place == 3:
                result[index] = "Bronze Medal"    
            else:
                result[index] = str(place)
            place += 1
        return result

