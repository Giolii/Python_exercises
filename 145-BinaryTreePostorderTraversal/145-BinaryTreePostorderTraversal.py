# Last updated: 7/25/2025, 3:53:38 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        stack1 = [root]
        stack2 = []
        result = []
        
        while stack1:
            node = stack1.pop()
            stack2.append(node)
            
            if node.left:
                stack1.append(node.left)
            if node.right:
                stack1.append(node.right)
        while stack2:
            result.append(stack2.pop().val)
        return result
        
        
#         result = []
        
#         def postorder(node):
#             if node:
#                 postorder(node.left)
#                 postorder(node.right)
#                 result.append(node.val)
#         postorder(root)
#         return result
        