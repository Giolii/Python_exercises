# Last updated: 7/10/2025, 4:46:34 PM
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        seen = {}
        
        def clone(node):
            if node in seen:
                return seen[node]
            
            copy = Node(node.val)
            seen[node] = copy
            
            for nei in node.neighbors:
                copy.neighbors.append(clone(nei))
            return copy
        return clone(node) if node else None
        
        
        
        
#         seen = {}
        
#         def dfs(node):
#             if node in seen:
#                 return seen[node]
            
#             copy = Node(node.val)
#             seen[node] = copy

#             for neigh in node.neighbors:
#                 copy.neighbors.append(dfs(neigh))
#             return copy
#         return dfs(node) if node else None

