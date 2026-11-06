class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        for slow in range(len(prices) -1):
            for fast in range(slow + 1, len(prices)):
                price = prices[fast] - prices[slow]

                if price > max_profit:
                    max_profit = price

        return max_profit