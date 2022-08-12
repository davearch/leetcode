# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.helper(root, res)
        return res

    def helper(self, root: Optional[TreeNode], res: list[int]) -> list[int]:
        if not root:
            return root
        self.helper(root.left, res)
        res.append(root.val)
        self.helper(root.right, res)