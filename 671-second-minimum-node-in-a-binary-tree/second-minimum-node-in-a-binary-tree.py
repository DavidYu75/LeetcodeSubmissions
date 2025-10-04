# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        unique_values = set()

        def dfs(root):
            if not root:
                return
            
            unique_values.add(root.val)
            dfs(root.left)
            dfs(root.right)

        dfs(root)
        unique_values = sorted(list(unique_values))
        
        return unique_values[1] if len(unique_values) >= 2 else -1
        
