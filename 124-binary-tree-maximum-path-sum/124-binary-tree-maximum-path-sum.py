# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        max_sum = root.val
        
        def mps(tree):
            nonlocal max_sum
            if not tree:
                return (float('-inf'), float('-inf'))
            lbs, ls = mps(tree.left)
            rbs, rs = mps(tree.right)
            
            mbs = max(tree.val + lbs, tree.val + rbs, tree.val)
            mts = max(tree.val, ls, rs, tree.val + rbs + lbs)
            max_sum = max(mbs, mts, max_sum)
            return (mbs, mts)
        
        mps(root)
        return max_sum