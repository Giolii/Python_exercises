# Last updated: 7/7/2025, 4:14:58 PM
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows,cols = len(grid),len(grid[0])
        visited = set()
        islands = 0
        
        def bfs(r,c):
            queue = deque([(r,c)])
            visited.add((r,c))
            
            directions = [(0,1),(1,0),(-1,0),(0,-1)]
            
            while queue:
                row,col = queue.popleft()
                
                for dr,dc in directions:
                    new_r, new_c = row + dr, col + dc
                    
                    if ( 0 <= new_r < rows and 0 <= new_c < cols and (new_r,new_c) not in visited and grid[new_r][new_c] == '1'):
                        visited.add((new_r,new_c))
                        queue.append((new_r,new_c))
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1' and (i,j) not in visited:
                    bfs(i,j)
                    islands += 1
        return islands