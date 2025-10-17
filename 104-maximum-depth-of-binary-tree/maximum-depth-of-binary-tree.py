# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # if not root:
        #     return 0
        
        # return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

        queue = deque()

        if root:
            queue.append(root)

        depth = 0

        while queue:
            for i in range(len(queue)):
                curr = queue.popleft()

                if curr.left:
                    queue.append(curr.left)
                
                if curr.right:
                    queue.append(curr.right)
            
            depth += 1
        
        return depth

        # time: O(n)
        # space: O(n)
