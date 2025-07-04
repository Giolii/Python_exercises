# Last updated: 6/30/2025, 4:59:46 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root or root.val == val:
            return root
        
        if val > root.val:
            return self.searchBST(root.right, val)
        else:
            return self.searchBST(root.left,val)
            