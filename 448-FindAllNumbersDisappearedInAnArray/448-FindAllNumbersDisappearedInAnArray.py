# Last updated: 6/25/2025, 11:43:13 AM
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        check = [0] * n
        missing = 0
        
        for num in nums:
            check[num - 1] = 1
        for i in range(n):
            if check[i] == 0:
                nums[missing] = i+1
                missing += 1
        return  nums[:missing]

        
        
        
# Input: nums = [4,3,2,7,8,2,3,1]
# Output: [5,6]

# Input: nums = [1,1]
# Output: [2]