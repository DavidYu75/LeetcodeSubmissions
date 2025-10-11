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
            
        #     return root1.val == root2.val and dfs(root1.left, root2.right) and dfs(root1.right, root2.left)
        
        # return dfs(root, root)

        def bfs(root1, root2):
            queue = deque()

            queue.append((root1, root2))

            while queue:
                for i in range(len(queue)):
                    node1, node2 = queue.popleft()

                    if node1 is None and node2 is None:
                        continue
                    if node1 is None or node2 is None:
                        return False
                    if node1.val != node2.val:
                        return False
                    
                    queue.append((node1.left, node2.right))
                    queue.append((node1.right, node2.left))
            
            return True
        
        return bfs(root, root)
        