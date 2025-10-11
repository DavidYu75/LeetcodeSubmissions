class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # go through every subarray in this array
        # keep track of the current sum of the subarray
        # compare it with a max sum
        # return the max sum
        # Time complexity of this solution: O(n^2) 
        # Space complexity: O(1)

        # max_sum = nums[0]

        # for i in range(len(nums)):
        #     curr_sum = 0
        #     for j in range(i, len(nums)):
        #         curr_sum += nums[j]
        #         max_sum = max(max_sum, curr_sum)
        
        # return max_sum

        # nums = [-2,1,-3,4,-1,2,1,-5,4]
        # -2 + 1 = -1
        # 1 + -3 = -2 + 4 = 2
        # -3 
        # 4

        # curr_sum, max_sum
        # curr_sum goes negative, we can start fresh with the next element
        # max_sum

        max_sum = nums[0]
        curr_sum = 0

        for num in nums:
            if curr_sum < 0:
                curr_sum = 0
            curr_sum += num
            max_sum = max(max_sum, curr_sum)
        
        return max_sum
        