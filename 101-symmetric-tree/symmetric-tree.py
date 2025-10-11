# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # def dfs(root1, root2):
        #     if root1 is None and root2 is None:
        #         return True
        #     if root1 is None or root2 is None:
        #         return False
        #     if root1.val != root2.val:
        #         return False
            
        #     return root1.val == root2.val and dfs(root1.left, root2.right) and dfs(root1.right, root2.left)

        # return dfs(root, root)

        queue = deque()

        queue.append((root, root))

        while queue:
            for i in range(len(queue)):
                root1, root2 = queue.popleft()

                if root1 is None and root2 is None:
                    continue
                if root1 is None or root2 is None:
                    return False
                if root1.val != root2.val:
                    return False
                
                queue.append((root1.left, root2.right))
                queue.append((root1.right, root2.left))
        
        return True
        