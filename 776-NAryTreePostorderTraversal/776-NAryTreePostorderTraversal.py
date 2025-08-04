# Last updated: 8/4/2025, 11:52:36 AM
"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        
        result = []
        node_stack = [root]
        rev_stack = []
        
        while node_stack:
            node = node_stack.pop()
            rev_stack.append(node)
            node_stack.extend(node.children)
        
        while rev_stack:
            node = rev_stack.pop()
            result.append(node.val)
        
        return result
        
