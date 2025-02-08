class Solution:
    # 1, 2, 3, 1
    # length = 4

    # 2 7 9 3 1
    # length = 5
    def rob(self, nums: List[int]) -> int:
        # total_houses = len(nums)
        # total_visits = math.ceil(total_houses / 2)

        # dp = [0] * (total_houses + 2)  # 0 0 0 0 0
        # # for i in range(total_houses):
        # #     dp[i] = nums[i]

        # print(dp)
        # print(dp[-1])
        # print(dp[-2])
        # # i = 4: dp[4] = nums[4] + dp[2]: 1 + 11 = 12
        # # i = 3: dp[3] = nums[3] + dp[1]: 3 + 7 = 10
        # # i = 2: dp[2] = nums[2] + dp[0]: 9 + 2 = 11
        # # i = 1: dp[1] = nums[1] + dp[-1]: 7 + 0 = 7
        # # i = 0: dp[0] = nums[0] + dp[-2]: 2 + 0 = 2
        # for i in reversed(range(total_houses)):
        #     print("i: ", i)
        #     print("nums[i]: ", nums[i])
        #     print("dp[i + 2]: ", dp[i - 2])
        #     dp[i] = nums[i] + dp[i-2]
        #     print("dp[i]: ", dp[i])
        #     print(dp)

        # return max(dp[0], dp[1])

        dp1, dp2 = 0, 0

        for num in nums:
            dp1, dp2 = dp2, max(dp1 + num, dp2)
        
        return dp2
        