# Last updated: 6/25/2025, 11:42:53 AM
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        max_from_right = arr[n - 1]
        for i in range(n - 2, -1, -1):
            current = arr[i]
            arr[i] = max_from_right
            max_from_right = max(max_from_right, current)
    
    # Last element becomes -1
        arr[n - 1] = -1
    
        return arr
    
    
    
#       Input: arr = [17,18,5,4,6,1]
#       Output: [18,6,6,6,1,-1]