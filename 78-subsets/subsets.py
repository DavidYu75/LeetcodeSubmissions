class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        curr_subset = []

        def dfs(i):
            if i >= len(nums):            
                result.append(curr_subset.copy())
                return
            
            # decision to add i
            curr_subset.append(nums[i])
            dfs(i + 1)

            # decision not to add
            curr_subset.pop()
            dfs(i + 1)

        dfs(0)
        return result
