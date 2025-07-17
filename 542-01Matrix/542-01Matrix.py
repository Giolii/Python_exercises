# Last updated: 7/16/2025, 6:14:15 PM
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m,n = len(mat), len(mat[0])
        
        for r in range(m):
            for c in range(n):
                if mat[r][c] > 0:
                    top = mat[r-1][c] if r > 0 else math.inf
                    left = mat[r][c-1] if c > 0 else math.inf
                    mat[r][c] = min(top,left) + 1
        
        for r in range(m-1,-1,-1):
            for c in range(n-1,-1,-1):
                if mat[r][c] > 0:
                    bottom = mat[r+1][c] if r < m - 1 else math.inf
                    right = mat[r][c+1] if c < n - 1 else math.inf
                    mat[r][c] = min(mat[r][c],bottom+1,right+1)
        return mat
        
        
        
#         m,n = len(mat), len(mat[0])
        
#         for r in range(m):
#             for c in range(n):
#                 if mat[r][c] > 0:
#                     top = mat[r - 1][c] if r > 0 else math.inf
#                     left = mat[r][c-1] if c > 0 else math.inf
#                     mat[r][c] = min(top,left) + 1
#         for r in range(m-1,-1,-1):
#             for c in range(n-1,-1,-1):
#                 if mat[r][c] > 0:
#                     bottom = mat[r + 1][c] if r < m -1 else math.inf
#                     right =  mat[r][c + 1] if c < n -1 else math.inf
#                     mat[r][c] = min(mat[r][c], bottom + 1, right + 1)
#         return mat
                
                    

        
        
        
        
#         if not mat or not mat[0]:
#             return mat
    
#         m,n = len(mat), len(mat[0])
#         DIR = [0,1,0,-1,0]
#         q = deque([])
    
#         for r in range(m):
#             for c in range(n):
#                 if mat[r][c] == 0:
#                     q.append((r,c))
#                 else:
#                     mat[r][c] = -1
                
#         while q:
#             r,c = q.popleft()
#             for i in range(4):
#                 nr,nc = r + DIR[i], c + DIR[i+1]
#                 if nr < 0 or nr == m or nc < 0 or nc == n or mat[nr][nc] != -1: continue
#                 mat[nr][nc] = mat[r][c] + 1
#                 q.append((nr,nc))
#         return mat
    