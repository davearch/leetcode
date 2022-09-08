# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        stack = [root]
        result = []
        while stack:
            curr = stack.pop()
            if curr:
                if isinstance(curr, str):
                    result.append(curr)
                    continue
                else:
                    result.append(str(curr.val))

                if curr.right:
                    stack.append(")")
                    stack.append(curr.right)
                    stack.append("(")
                if not curr.left and curr.right:
                    stack.append("()")
                if curr.left:
                    stack.append(")")
                    stack.append(curr.left)
                    stack.append("(")

        return ''.join(result)