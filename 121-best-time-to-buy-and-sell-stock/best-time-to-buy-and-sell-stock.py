class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # curr_max = 0
        # global_max = 0

        # for i in range(1, len(prices)):
        #     curr_max += prices[i] - prices[i - 1]
        #     curr_max = max(0, curr_max)
        #     global_max = max(curr_max, global_max)

        # return global_max

        left = 0
        right = 1
        max_profit = 0

        while right < len(prices):
            current_profit = prices[right] - prices[left]

            if prices[left] < prices[right]:
                max_profit = max(current_profit, max_profit)
            else:
                left = right

            right += 1

        return max_profit