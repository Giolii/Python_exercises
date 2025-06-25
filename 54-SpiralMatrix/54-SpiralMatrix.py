# Last updated: 6/25/2025, 11:43:40 AM
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        
        m,n = len(matrix), len(matrix[0])
        row,col = 0,0
        result = []
        going_right = True
        going_down = False
        going_up  = False
        going_left = False
        skip = 0
        
        for i in range(m*n):
            result.append(matrix[row][col])
            # print(matrix[row][col])
            if going_right:
                if col == n -1 - skip:
                    row += 1
                    going_right = False
                    going_down = True
                else:
                    col += 1
            elif going_down:
                if row == m - 1 - skip:
                    col -= 1
                    going_down = False
                    going_left = True
                else:
                    row += 1
            elif going_left:
                if col == 0 + skip:
                    row -= 1
                    going_left = False
                    going_up = True
                    skip+= 1
                else:
                    col -= 1
            elif going_up:
                if row == 0 + skip:
                    col += 1
                    going_up = False
                    going_right = True
                else:
                    row -= 1
        return result
                    
                    
            
            
            
            
        
        