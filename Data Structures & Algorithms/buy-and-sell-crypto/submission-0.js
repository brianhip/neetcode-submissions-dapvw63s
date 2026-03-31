class Solution {
    /**
     * @param {number} prices
     * @return {number}
     */
    maxProfit(prices) {
        // Use a variable to keep track of the maximum profit
        let maximumProfit = 0;
        // Iterate throught the prices and have a buy and sell index
        let buy = 0;
        let sell = 0;
        for (let i = 0; i < prices.length; i++) {
            if (prices[buy] > prices[i]) {
                buy = i;
                sell = i;
            } else if (prices[sell] < prices[i]) {
                sell = i;
                maximumProfit = Math.max(prices[sell]-prices[buy], maximumProfit);
            }
        }
        return maximumProfit;

    }
}
