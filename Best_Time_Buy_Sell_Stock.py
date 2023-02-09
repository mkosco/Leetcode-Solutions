class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        sell = 1
        maxProfit = 0

        while sell < len(prices):
            currentProfit = prices[sell] - prices[buy]
            if prices[buy] < prices[sell]:
                maxProfit = max(maxProfit, currentProfit)
            else:
                buy = sell
            sell += 1
        return maxProfit 