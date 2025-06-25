# Last updated: 6/25/2025, 11:43:46 AM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy= ListNode(0,head)
        slow = dummy
        fast = dummy
        
        for i in range(n + 1):
            fast = fast.next
        while fast:
            fast=fast.next
            slow=slow.next

        slow.next = slow.next.next
        return dummy.next
        
        
#       [1,2,3,4,5] n = 2