# Last updated: 8/9/2025, 3:44:16 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        # if val < root.val:
        #     root.left = self.insertIntoBST(root.left,val)
        # else:
        #     root.right = self.insertIntoBST(root.right,val)
        # return root
        
        current = root
        while current:
            if current.val < val:
                if not current.right:
                    current.right = TreeNode(val)
                    break
                current = current.right
            else:
                if not current.left:
                    current.left = TreeNode(val)
                    break
                current = current.left
        return root