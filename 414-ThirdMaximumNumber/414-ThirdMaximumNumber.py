# Last updated: 6/25/2025, 11:43:14 AM
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        first = None
        second = None
        third = None
        
        for i in range(len(nums)):
            if nums[i] in [first, second, third]:
                continue
            if not first or nums[i] > first:
                third = second
                second = first
                first = nums[i]
            elif not second or nums[i] > second:
                third = second
                second = nums[i]
            elif not third or nums[i] > third:
                third = nums[i]
        print(first,second,third)
        if third != None:
            return third
        else:
            return first
        