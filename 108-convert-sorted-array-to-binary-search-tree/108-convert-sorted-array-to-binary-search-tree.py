# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, nums, lo, hi):
        if lo > hi:
            return None
        mid = (lo + hi) // 2
        node = TreeNode(nums[mid])
        node.left = self.helper(nums, lo, mid-1)
        node.right = self.helper(nums, mid+1, hi)
        return node
        
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        """
                0
             -3     9
         -10      5
        [-10,-3,0,5,9]
        """
        return self.helper(nums, 0, len(nums)-1)
