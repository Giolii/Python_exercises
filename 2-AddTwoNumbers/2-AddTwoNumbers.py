# Last updated: 6/25/2025, 11:43:57 AM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = result =  ListNode(0)
        carry = 0

        while l1 or l2 or carry: 
            num1 = l1.val if l1 else 0
            num2 = l2.val if l2 else 0
            
            sum = num1 + num2 + carry
            carry = sum // 10
            
            result.next = ListNode(sum % 10)
            result = result.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        
        return dummy.next
    
    
#     [2,4,3]
#     [5,6,4]
    