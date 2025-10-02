class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def backtrack(i, nums, curr_set, result):
            if i >= len(nums):
                result.append(curr_set.copy())
                return
            
            curr_set.append(nums[i])
            backtrack(i + 1, nums, curr_set, result)
            curr_set.pop()

            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            
            backtrack(i + 1, nums, curr_set, result)
        
        nums.sort()
        curr_set, result = [], []
        backtrack(0, nums, curr_set, result)
        return result
