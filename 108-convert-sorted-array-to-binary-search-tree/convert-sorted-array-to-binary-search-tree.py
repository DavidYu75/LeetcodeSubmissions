# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # if not nums:
        #     return None

        # middle = len(nums) // 2

        # root = TreeNode(nums[middle])
        # root.left = self.sortedArrayToBST(nums[:middle])
        # root.right = self.sortedArrayToBST(nums[middle+1:])

        # return root

        def convert(left, right):
            if left > right:
                return None
        
            middle = (left + right) // 2
            node = TreeNode(nums[middle])
            node.left = convert(left, middle - 1)
            node.right = convert(middle + 1, right)

            return node

        return convert(0, len(nums) - 1)

        

