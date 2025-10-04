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

        current_node = root
        previous_right_node = None
        parent_node = None

        while current_node:
            left_node = current_node.left
            right_node = current_node.right

            current_node.left = previous_right_node
            current_node.right = parent_node

            previous_right_node = right_node
            parent_node = current_node
            current_node = left_node

        return parent_node
        