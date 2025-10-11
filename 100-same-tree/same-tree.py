# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queue = deque()
        
        queue.append((p, q))

        while queue:
            for i in range(len(queue)):
                p, q = queue.popleft()

                if p is None and q is None:
                    continue
                if p is None or q is None:
                    return False
                if p.val != q.val:
                    return False
                
                queue.append((p.left, q.left))
                queue.append((p.right, q.right))
        
        return True


        # if p is None and q is None:
        #     return True
        # if p is None or q is None:
        #     return False
        # if p.val != q.val:
        #     return False
        
        # return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)