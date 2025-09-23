class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # nums = 1, 1, 1
        # prefix = 1, 2, 3

        # result = 0

        # for i in range(len(nums)):
        #     subarray_total = 0
        #     for j in range(i, len(nums)):
        #         subarray_total += nums[j]
        #         if subarray_total == k:
        #             result += 1
        
        # return result

        result = 0
        prefix_map = {0: 1}
        prefix_total = 0

        for num in nums:
            prefix_total += num
            sum_needed = prefix_total - k

            if sum_needed in prefix_map:
                result += prefix_map[sum_needed]
            
            prefix_map[prefix_total] = 1 + prefix_map.get(prefix_total, 0)
        
        return result