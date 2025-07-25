# Last updated: 7/25/2025, 3:53:46 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node,cur):
            if not node:
                return False
            
            cur += node.val
            
            if not node.right and not node.left:
                return cur == targetSum
            
            return dfs(node.left,cur) or dfs(node.right,cur)
        return dfs(root,0)