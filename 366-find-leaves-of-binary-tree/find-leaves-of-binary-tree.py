# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = defaultdict(list)

        def dfs(root, layer):
            if not root:
                return layer
            
            left = dfs(root.left, layer)
            right = dfs(root.right, layer)

            layer = max(left, right)
            result[layer].append(root.val)

            return layer + 1
        
        dfs(root, 0)

        return list(result.values())
