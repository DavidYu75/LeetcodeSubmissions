class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr_max = 0
        global_max = 0

        for i in range(1, len(prices)):
            curr_max += prices[i] - prices[i - 1]
            curr_max = max(0, curr_max)
            global_max = max(curr_max, global_max)

        return global_max