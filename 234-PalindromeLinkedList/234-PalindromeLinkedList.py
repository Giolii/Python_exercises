# Last updated: 6/25/2025, 11:43:20 AM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
#         Edge case
        if not head or not head.next:
            return True
        
#         Find half
        slow = head
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

#         Reorder
        first = head
        second = self.reverse(slow)

#         Compare
        while second:
            if first.val != second.val:
                return False
            else:
                first = first.next
                second = second.next
        return True
        
    def reverse(self,head):
        prev = None
        curr = head
        
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev
        
        
        