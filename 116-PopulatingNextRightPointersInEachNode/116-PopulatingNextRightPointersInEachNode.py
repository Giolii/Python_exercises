# Last updated: 7/25/2025, 3:53:48 PM
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
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root: return None
        L,R,N = root.left, root.right, root.next
        
        if L:
            L.next = R
            if N: R.next = N.left
            self.connect(L)
            self.connect(R)
        return root
        
        
#         if not root: return None
#         q = deque([root])
        
#         while q:
#             rightNode = None
#             for _ in range(len(q)):
#                 cur = q.popleft()
#                 cur.next = rightNode
#                 rightNode = cur
#                 if cur.right:
#                     q.extend([cur.right,cur.left])
#         return root