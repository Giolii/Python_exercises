# Last updated: 6/28/2025, 3:20:10 PM
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        my_map = {}
        for num1 in nums1:
            for num2 in nums2:
                sum12 = num1 + num2
                my_map[sum12] = my_map.get(sum12, 0 ) + 1
        
        count = 0
        for num3 in nums3:
            for num4 in nums4:
                sum34 = num3 + num4
                target = -sum34
                count += my_map.get(target,0)
                
        return count