class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # n = 3
        # nums[1] = nums[(1 + 1) % 3] = nums[2]
        # nums[3] = nums[(3 + 1) % 3] = nums[1]

        # 1 - 2 = -1
        # 3
        # 3 - 2 = 1
        # 1 + 1 - 2 + 3 = 3

        global_max, global_min = nums[0], nums[0]
        curr_max, curr_min = 0, 0
        total = 0

        for n in nums:
            curr_max = max(n, curr_max + n)
            curr_min = min(n, curr_min + n)
            total += n
            global_max = max(global_max, curr_max)
            global_min = min(global_min, curr_min)

        if global_max < 0:
            return global_max
        else:
            return max(global_max, total - global_min)
            