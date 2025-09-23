class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # prefix: 1, 8, 11, 17, 22, 28
        # postfix: 28, 27, 20, 17, 11, 6
        # space: O(2n) = O(n)
        # time: O(n) + O(n) = O(n)

        # prefix: 2, 3, 2
        # postfix: 2 0 -1

        prefix, postfix = [], []
        prefix_total, postfix_total = 0, 0

        for num in nums:
            prefix_total += num
            prefix.append(prefix_total)

        for num in reversed(nums):
            postfix_total += num
            postfix.append(postfix_total)

        postfix = list(reversed(postfix))

        for i in range(len(prefix)):
            if prefix[i] == postfix[i]:
                return i
        
        return -1
