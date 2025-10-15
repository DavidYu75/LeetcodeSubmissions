class Solution:
    def rob(self, nums: List[int]) -> int:
        # time: O(n)
        # space: O(n)

        if len(nums) == 1:
            return nums[0]

        memo = {}

        def dfs(i, first_house):
            if (i == len(nums) - 1 and first_house) or i >= len(nums):
                return 0
            
            if (i,first_house) in memo:
                return memo[(i,first_house)]
            
            memo[(i,first_house)] = max(dfs(i+1, first_house), nums[i] + dfs(i+2, first_house or i == 0))

            return memo[(i,first_house)]
        
        return max(dfs(0, True), dfs(1, False))
        