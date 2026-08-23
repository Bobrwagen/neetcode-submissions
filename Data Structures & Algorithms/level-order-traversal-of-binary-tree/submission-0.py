# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = [root]
        res = []
        while queue:
            res.append([q.val for q in queue])
            new_queue = []
            for el in queue:
                if el.left:
                    new_queue.append(el.left)
                if el.right:
                    new_queue.append(el.right)
            queue = new_queue
        return res

        