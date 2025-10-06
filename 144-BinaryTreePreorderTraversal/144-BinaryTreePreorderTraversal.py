# Last updated: 7/25/2025, 3:53:39 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        stack = [root]
        if not root:
            return result
        
        while stack:
            node = stack.pop()
            result.append(node.val)
            
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return result
        
        
        # result = []
        # def preord(node):
        #     if node:
        #         result.append(node.val)
        #         preord(node.left)
        #         preord(node.right)
        # preord(root)
        # return result
        
