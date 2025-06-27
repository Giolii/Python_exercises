# Last updated: 6/27/2025, 11:53:38 AM
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for row in board:
            if not self.is_valid(row):
                return False
        for col in range(9):
            column = [board[row][col] for row in range(9)]
            if not self.is_valid(column):
                return False
        
        for box_row in range(0,9,3):
            for box_col in range(0,9,3):
                sub_box = []
                for i in range(box_row, box_row + 3):
                    for j in range(box_col, box_col + 3):
                        sub_box.append(board[i][j])
                if not self.is_valid(sub_box):
                    return False
        return True
                
        

    
    def is_valid(self,unit):
        filled_cells = [cell for cell in unit if cell != '.']
        return len(filled_cells) == len(set(filled_cells))
            