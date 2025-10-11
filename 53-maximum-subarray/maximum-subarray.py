class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_result = nums[0]
        curr_result = 0

        for i in range(len(nums)):
            if curr_result < 0:
                curr_result = 0

            curr_result += nums[i]
            max_result = max(max_result, curr_result)
        
        return max_result
        