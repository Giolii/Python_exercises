# Last updated: 7/25/2025, 3:53:45 PM
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return 
        current_level_node = root
        next_level_dummy = Node(0)
        next_level_builder = next_level_dummy
        
        while current_level_node is not None:
            if current_level_node.left is not None:
                next_level_builder.next = current_level_node.left
                next_level_builder = next_level_builder.next
                
            if current_level_node.right is not None:
                next_level_builder.next = current_level_node.right
                next_level_builder = next_level_builder.next
            
            if current_level_node.next is not None:
                current_level_node = current_level_node.next
            else:
                current_level_node = next_level_dummy.next
                next_level_dummy.next = None
                next_level_builder = next_level_dummy
        return root
                    