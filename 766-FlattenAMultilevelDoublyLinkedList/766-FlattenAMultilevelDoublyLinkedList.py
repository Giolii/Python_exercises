# Last updated: 6/25/2025, 11:43:02 AM
"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        
        current = head

        while current:
            if current.child:
                self.sub_node_handle(current.child,current)
            else:
                current = current.next

        return head
    
    def sub_node_handle(self,sub,current):
        current.child = None 
        next_node = current.next
        while sub:
            sub.prev = current 
            current.next = sub
            current = current.next
            if sub.child:
                self.sub_node_handle(sub.child,current)
            sub = sub.next
            if next_node :
                next_node.prev = current
        current.next = next_node
        current = current.next