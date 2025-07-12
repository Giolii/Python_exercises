# Last updated: 7/12/2025, 1:33:06 PM
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        base = image[sr][sc]
        if base == color:
            return image
        
        def dfs(image,sr,sc,color):
            if sr < 0 or sc < 0 or sr >= len(image) or sc >= len(image[0]) or image[sr][sc] != base:
                return
        
            image[sr][sc] = color
            dfs(image,sr+1,sc,color)
            dfs(image,sr-1,sc,color)
            dfs(image,sr,sc+1,color)
            dfs(image,sr,sc-1,color)
        dfs(image,sr,sc,color)
        return image
        