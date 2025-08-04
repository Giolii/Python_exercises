# Last updated: 8/4/2025, 11:52:38 AM
"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        # self.max_depth = 0
        # def dfs(node,depth):
        #     if not node: return
        #     self.max_depth = max(self.max_depth,depth)
        #     for child in node.children:
        #         dfs(child,depth+1)
        # dfs(root,1)
        # return self.max_depth
        
        if not root: return 0
        if not root.children: return 1
        return 1 + max(self.maxDepth(child) for child in root.children)
    
        