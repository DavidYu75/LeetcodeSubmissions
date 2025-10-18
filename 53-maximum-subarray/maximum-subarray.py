class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # brute force:
        # generate all possible subarrays from the nums array
        # keep track of the sum of each subarray and the greatest sum we get from a subarray
        # time: O(n^2)
        # space: O(1)

        # max_sum = 0

        # for i in range(len(nums)):
        #     curr_sum = 0
        #     for j in range(i, len(nums)):
        #         curr_sum += nums[j]

        #         max_sum = max(max_sum, curr_sum)
        
        # return max_sum

        # keep track of our current sum as we going through the array
        # if our current sum ever ends up negative, reset our current sum to 0, just start from the next number
        # O(n)
        # O(1)
        # -2, 1, -3, -1, 2, 1, -5, 4
        # -2 + 1 = -1
        # -1 + -3 = -4
        # -4 + 4 = 0
        # 0 + -1 = -1
        # -1 + 2 = 1
        # 1 + -5 = -4
        # -4 + 4 = 0

        # nums = [-1]
        max_sum = nums[0]
        curr_sum = 0

        for num in nums:
            if curr_sum < 0:
                curr_sum = 0
            
            curr_sum += num

            max_sum = max(max_sum, curr_sum)
        
        return max_sum