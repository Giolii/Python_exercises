# Last updated: 9/21/2025, 12:20:38 PM
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1,set2 = set(nums1),set(nums2)
        result = [[],[]]
        # ans1 = list(set1-set2)
        # ans2 = list(set2-set1)

        for i in set1:
            if i not in set2:
                result[0].append(i)
        for i in set2:
            if i not in set1:
                result[1].append(i)
        return result
