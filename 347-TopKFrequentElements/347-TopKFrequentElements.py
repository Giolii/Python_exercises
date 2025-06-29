# Last updated: 6/29/2025, 2:17:09 PM
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map_nums ={}
        result = []
        high = 0
        temp= 0
        
        for num in nums:
            map_nums[num] = map_nums.get(num,0) + 1
        
        for i in range(k):
            high = 0
            temp = 0
            for key in map_nums:
                if map_nums[key] > high:
                    temp = key
                    high = map_nums[key]
            result.append(temp)
            del map_nums[temp]

        return result