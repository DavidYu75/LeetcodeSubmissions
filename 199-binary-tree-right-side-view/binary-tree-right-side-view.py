# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        queue = deque()

        if not root:
            return result

        queue.append(root)
        
        while len(queue) > 0:
            right_side = None

            for i in range(len(queue)):
                curr = queue.popleft()
                
                if curr:
                    right_side = curr
                    queue.append(curr.left)
                    queue.append(curr.right)

            if right_side:
                result.append(right_side.val)
                
        return result

                