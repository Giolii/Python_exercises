# Last updated: 6/25/2025, 6:02:40 PM
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2) )