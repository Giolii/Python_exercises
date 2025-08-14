# Last updated: 8/13/2025, 5:15:03 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def inorder(node):
            if not node: return True
            if not inorder(node.left): return False
            if self.prev is not None and node.val<= self.prev:
                return False
            self.prev = node.val
            return inorder(node.right)
        self.prev = None 
        return inorder(root)
        
        
        
        
        # def validate(node,min,max):
        #     if not node: return True
        #     if node.val >= max or node.val <= min: return False
        #     return validate(node.left,min,node.val) and validate(node.right,node.val,max)
        # return validate(root,float(-inf),float(inf))