# Last updated: 6/25/2025, 11:43:34 AM
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        triangle = []
        for i in range(numRows):
            row = [1]
            
            for j in range(1,i):
                row.append(triangle[i-1][j-1] + triangle[i-1][j])
                
            if i > 0:
                row.append(1)
                
            triangle.append(row)
        return triangle
            