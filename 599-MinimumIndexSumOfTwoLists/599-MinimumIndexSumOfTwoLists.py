# Last updated: 6/26/2025, 11:33:21 AM
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        map1={}
        map3 ={}
        lower = float('inf')
        result = []
        
        for i,char in enumerate(list1):
            map1[char] = i
            
        for i,char in enumerate(list2):
            if char in map1:
                sum_i = map1[char] + i
                map3[char] = sum_i
                if sum_i == lower:
                    result.append(char)
                if sum_i < lower:
                    result = [char]
                    lower = map3[char]
        return result