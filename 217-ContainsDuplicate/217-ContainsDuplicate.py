# Last updated: 6/25/2025, 3:12:25 PM
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        my_set = set()
        for num in nums:
            if num in my_set:
                return True
            else: 
                my_set.add(num)
        return False
        