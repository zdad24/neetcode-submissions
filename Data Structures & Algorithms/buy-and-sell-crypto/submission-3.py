class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        sell = 1
        maxprofit, profit = 0, 0
        while (sell < len(prices)):
            profit = prices[sell] - prices[buy]
            maxprofit = max(maxprofit, profit)
            if (prices[sell] < prices[buy]):
                buy=sell
                sell+=1
            else:
                sell+=1

        return maxprofit