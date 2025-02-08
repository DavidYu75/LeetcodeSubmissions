class Solution:
    # 10, 15, 20
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)   # 3
        dp = [0] * (n + 2)  # 0 0 0 0 0

        # i = 2: dp[2] = cost[2] + min(dp[3], dp[4]): 20 + min(0, 0): 20
        # i = 1: dp[1] = cost[1] + min(dp[2], dp[3]): 15 + min(20, 0): 15 + 0
        # i = 0: dp[0] = cost[0] + min(dp[1], dp[2]): 10 + min(15, 20): 25
        # dp = 25, 15, 20, 0, 0
        for i in reversed(range(n)):
            dp[i] = cost[i] + min(dp[i + 1], dp[i + 2])

        return min(dp[0], dp[1])