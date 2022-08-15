# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        stack = [(1, root)]
        maxDepth = 0
        while stack:
            depth, curr = stack.pop()
            if curr:
                maxDepth = max(maxDepth, depth)
                stack.append((depth +1, curr.left))
                stack.append((depth +1, curr.right))
        return maxDepth