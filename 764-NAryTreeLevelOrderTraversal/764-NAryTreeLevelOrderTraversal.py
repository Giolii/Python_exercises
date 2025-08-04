# Last updated: 8/4/2025, 11:52:40 AM
"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root: return
        result = []
        
        def dfs(node,level):
            if len(result) == level:
                result.append([])
            result[level].append(node.val)
            
            for child in node.children:
                dfs(child,level+1)
        dfs(root,0)
        return result
        
        
        
        
#         if not root: return []
        
#         result = []
#         q = deque([root])
#         while q:
#             level = []
#             for _ in range(len(q)):
#                 node = q.popleft()
#                 level.append(node.val)
#                 q.extend(node.children)
#             result.append(level)
#         return result
                