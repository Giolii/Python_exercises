# Last updated: 7/21/2025, 3:20:52 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []

        for i,head in enumerate(lists):
            if head:
                heappush(heap,(head.val,i,head))

        dummy = ListNode(0)
        current = dummy
        
        while heap:
            val, list_idx, node = heappop(heap)
            current.next = node
            current = current.next

            if node.next:
                heappush(heap,(node.next.val,list_idx,node.next))
        return dummy.next

