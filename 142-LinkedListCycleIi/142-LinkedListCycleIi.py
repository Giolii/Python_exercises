# Last updated: 6/25/2025, 11:43:30 AM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow = head
        start = head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break
        else:    
            return None
        
        while start != slow:
            start = start.next
            slow = slow.next
        return start
        
            