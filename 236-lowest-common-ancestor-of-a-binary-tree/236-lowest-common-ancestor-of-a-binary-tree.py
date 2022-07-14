# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        # variable to store LCA node.
        self.ans = None
    
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def recurse_tree(current_node):
            # if reached the end of a branch, return False.
            if not current_node:
                return False
            
            # left recursion
            left = recurse_tree(current_node.left)
            
            # right recursion
            right = recurse_tree(current_node.right)
            
            # if the current node is one of p or q
            mid = current_node == p or current_node == q
            
            # if any two of the three flags left, right or mid become True
            if mid + left + right >= 2:
                self.ans = current_node
            
            # return True if either of the three bool values is True
            return mid or left or right
        
        # traverse the tree
        recurse_tree(root)
        return self.ans