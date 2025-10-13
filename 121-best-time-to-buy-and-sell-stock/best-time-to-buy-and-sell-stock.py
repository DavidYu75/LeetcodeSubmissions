import math
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        lowest_stock = prices[0]

        for price in prices:
            lowest_stock = min(lowest_stock, price)
            max_profit = max(max_profit, price - lowest_stock)
        
        return max_profit
        