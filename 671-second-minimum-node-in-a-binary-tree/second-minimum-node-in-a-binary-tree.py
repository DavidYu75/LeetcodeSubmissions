# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        min_val = root.val
        self.second_min_val = float('inf')

        def dfs(root):
            if not root:
                return
            
            if min_val < root.val < self.second_min_val:
                self.second_min_val = root.val
            
            if root.val < self.second_min_val:
                dfs(root.left)
                dfs(root.right)
        
        dfs(root)

        return self.second_min_val if self.second_min_val != float('inf') else -1 