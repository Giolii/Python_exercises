# Last updated: 7/25/2025, 3:53:49 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder:
            return None
        root = TreeNode(postorder.pop())
        mid = inorder.index(root.val)
        root.right = self.buildTree(inorder[mid+1:],postorder) 
        root.left = self.buildTree(inorder[:mid],postorder)
        return root