# Last updated: 6/25/2025, 11:43:32 AM
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        
        current = head
        
        while current:
            new_node = Node(current.val,current.next,None)
            current.next = new_node
            current = current.next.next
        current = head
        
        while current:
            current.next.random = current.random.next if current.random else None
            current = current.next.next
        head = head.next
        current = head
        
        while current:
            current.next = current.next.next if current.next else None
            current = current.next
            
        return head
        
        