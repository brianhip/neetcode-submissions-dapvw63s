class Solution {
    /**
     * @param {number} prices
     * @return {number}
     */
    maxProfit(prices) {
        let buy = prices[0];
        let sell = prices[0];
        let maxProfit = -Infinity;
        for(let i = 0; i < prices.length; i++) {
            if(prices[i] < buy) {
                buy = prices[i];
                sell = buy;
            }  
            if (prices[i] > sell){
                sell = prices[i];
                maxProfit = Math.max(sell-buy, maxProfit);
            }
        }
        return Math.max(sell-buy, maxProfit);       
    }
}
