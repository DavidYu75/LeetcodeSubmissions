class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 1
        # prefix: 1
        # suffix: 2 * 3 * 4 = 24

        # 3
        # prefix: 2 * 1 = 2
        # suffix: 4 = 4

        # prefix: [1, 1, 2, 6]
        # suffix: [24, 12, 4, 1]

        n = len(nums)
        result = [0] * n
        prefix = [0] * n
        suffix = [0] * n

        prefix[0] = suffix[n - 1] = 1

        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i - 1]
        
        for i in range(n - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]

        for i in range(len(suffix)):
            result[i] = prefix[i] * suffix[i]

        return result
