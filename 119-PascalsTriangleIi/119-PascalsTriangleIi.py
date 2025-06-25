# Last updated: 6/25/2025, 11:43:33 AM
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]
        
        for k in range(1, rowIndex + 1):
            next_val = row[k-1] * (rowIndex - k + 1) // k
            row.append(next_val)
        return row
            