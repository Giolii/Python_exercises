# Last updated: 6/25/2025, 11:43:24 AM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        node = dummy
        while node and node.next :
            if node.next and node.next.val == val:
                node.next = node.next.next if node.next else None
            else:
                node = node.next
        return dummy.next