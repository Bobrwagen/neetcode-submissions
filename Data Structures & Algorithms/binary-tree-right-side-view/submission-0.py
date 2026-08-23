# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        queue = [root]
        while queue:
            res.append(queue[-1].val)
            new_queue = []
            for el in queue:
                if el.left:
                    new_queue.append(el.left)
                if el.right:
                    new_queue.append(el.right)
            queue = new_queue
        return res