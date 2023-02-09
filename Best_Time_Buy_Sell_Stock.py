class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0;
        for i in range(len(prices)):
            currentProfit = max(prices[i:]) - prices[i]
            if result < currentProfit:
                result = currentProfit
        return result