# Last updated: 6/27/2025, 11:53:04 AM
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        seen= defaultdict(int)
        solution = []
        
        for num in nums1:
            # if num in seen:
            seen[num] += 1
            # else:
            #     seen[num] = 1
        
        for num in nums2:
            if num in seen and seen[num] >= 1:
                solution.append(num)
                seen[num] -= 1
        return solution
                