class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # update the buy when we find a better buy (cheaper)
        # calculate the current profit with the current day (sell - buy)
        # cache the best profit based on current profits
        max_profit = 0
        buy = 0
        for current in range(1, len(prices)):
            profit = prices[current] - prices[buy]
            max_profit = max(max_profit, profit)
            if prices[buy] > prices[current]:
                buy = current
        return max_profit
