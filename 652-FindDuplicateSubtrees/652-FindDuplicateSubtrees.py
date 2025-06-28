# Last updated: 6/28/2025, 3:20:07 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        subtree_count = defaultdict(int)
        result = []
        
        def serialize(node):
            if not node:
                return None
            left_serial = serialize(node.left)
            right_serial = serialize(node.right)
            subtree_serial = f"{node.val},{left_serial},{right_serial}"
        
            subtree_count[subtree_serial] += 1
            if subtree_count[subtree_serial] == 2:
                result.append(node)
            
            return subtree_serial
        serialize(root)
        return result