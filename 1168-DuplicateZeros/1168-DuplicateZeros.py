# Last updated: 6/25/2025, 11:42:54 AM
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        length = len(arr)
        i=0
        
        while i < length:
            if arr[i] == 0:
                for j in range(length-1, i,-1):
                    arr[j] = arr[j -1]
                if i+1 < length:
                    arr[i+1] = 0
                i += 2
            else:
                i += 1