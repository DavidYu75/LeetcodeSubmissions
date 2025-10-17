class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = nums[0]
        curr_sum = 0

        for num in nums:
            if curr_sum < 0:
                curr_sum = 0
            
            curr_sum += num
            result = max(result, curr_sum)
        
        return result