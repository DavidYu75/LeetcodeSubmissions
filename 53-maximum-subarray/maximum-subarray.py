class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # n, result = len(nums), nums[0]

        # for i in range(n):
        #     curr_result = 0
        #     for j in range(i, n):
        #         curr_result += nums[j]
        #         result = max(result, curr_result)
        
        # return result

        result = nums[0]
        curr_result = 0

        for num in nums:
            if curr_result < 0:
                curr_result = 0
            
            curr_result += num
            result = max(result, curr_result)
        
        return result
        