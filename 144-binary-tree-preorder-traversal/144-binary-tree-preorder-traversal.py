# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.dfs(root, res)
        return res
    
    def dfs(self, root: Optional[TreeNode], result: list[int]) -> None:
        if root:
            result.append(root.val)
            self.dfs(root.left, result)
            self.dfs(root.right, result)
