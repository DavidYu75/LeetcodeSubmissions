# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # binary search O(logn)

        # example 1:
        # root, p is less than the root and q is greater than the root
        # p is in the left subtree
        # q is in the right subtree
        # return root

        # example 2:
        # root = 6, p = 2, q = 4
        # root = 6, p = 7, q = 10
        # p is less than root and q is also less than root
        # p and q would both be in the left subtree
        # whenever p and q diverge and go into different paths, we return the root

        # recursion and dfs
        # base case: if not root return None

        # max(p, q) < root, search left
        # min(p, q) > root, search right
        # if p and q differ, return root

        if not root:
            return None
        
        if max(p.val, q.val) < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif min(p.val, q.val) > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root
        
        # time: O(logn)
        # space: O(h)
