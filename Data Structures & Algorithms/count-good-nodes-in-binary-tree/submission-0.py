# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.helper(root, -101)
    
    def helper(self, root, m):
        if not root:
            return 0
        
        res = 1 if root.val >= m else 0
        new_m = max(root.val, m)
        return res + self.helper(root.left, new_m) + self.helper(root.right, new_m)
        

        