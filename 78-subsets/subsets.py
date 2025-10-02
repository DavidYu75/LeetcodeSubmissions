class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(i, nums, result, curr_set):
            if i >= len(nums):
                result.append(curr_set.copy())
                return
            
            curr_set.append(nums[i])
            backtrack(i + 1, nums, result, curr_set)
            curr_set.pop()

            backtrack(i + 1, nums, result, curr_set)
        
        result, curr_set = [], []
        backtrack(0, nums, result, curr_set)
        return result