class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum = 0
        max_sum = nums[0]

        for n in nums:
            curr_sum = max(0, curr_sum)
            curr_sum += n
            max_sum = max(curr_sum, max_sum)
        
        return max_sum