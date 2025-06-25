# Last updated: 6/25/2025, 11:43:10 AM
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []
        m,n = len(mat),len(mat[0])
        result = []
        going_up = True
        row,col = 0,0
        
        for _ in range(m*n):
            result.append(mat[row][col])
            if going_up:
                if col == n - 1:
                    row += 1
                    going_up = False
                elif row == 0:
                    col += 1
                    going_up = False
                else:
                    row -= 1
                    col += 1
            else:
                if row == m - 1:
                    col += 1
                    going_up = True
                elif col == 0:
                    row += 1
                    going_up = True
                else:
                    row += 1
                    col -= 1
        return result
        
        