# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def dfs(root1, root2):
            if not root1 and not root2:
                return True
            
            if not root1 or not root2:
                return False
            
            if root1.val != root2.val:
                return False
            
            return dfs(root1.left, root2.right) and dfs(root1.right, root2.left)
        
        return dfs(root, root)

        def bfs(root1, root2):
            queue = deque([(root1, root2)])

            while queue:
                for i in range(len(queue)):
                    node1, node2 = queue.popleft()

                    if not node1 and not node2:
                        continue 

                    if not node1 or not node2:
                        return False

                    if node1.val != node2.val:
                        return False
                    
                    queue.append((node1.left, node2.right))
                    queue.append((node1.right, node2.left))
            
            return True
        
        return bfs(root, root)


        