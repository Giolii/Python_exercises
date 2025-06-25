# Last updated: 6/25/2025, 11:43:28 AM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a = headA
        b= headB
        change = False
        
        while a != b:
            a = a.next if a else headB
            b = b.next if b else headA
        return a
        

        