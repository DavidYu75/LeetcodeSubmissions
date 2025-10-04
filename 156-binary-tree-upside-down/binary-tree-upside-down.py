# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # previous left child becomes the root
        # previous root becomes the right child
        # previous right child becomes the left child
        
        current_node, previous_parent, previous_right = root, None, None

        while current_node:
            left_node, right_node = current_node.left, current_node.right

            current_node.left = previous_right
            current_node.right = previous_parent

            previous_right = right_node
            previous_parent = current_node
            current_node = left_node

        
        return previous_parent
        