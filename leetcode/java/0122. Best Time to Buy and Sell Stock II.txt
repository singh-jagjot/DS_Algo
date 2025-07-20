//  Why it works?
//  1) You are allowed to buy and sell as many times as you like, but you can’t hold multiple stocks at once;
//  2) You must sell before buying again.
//  3) You want to maximize profit, and every time there's a price increase from one day to the next,
//  it's a profitable opportunity.
//  4) The profit from multiple transactions (buy low, sell high) can be accumulated by summing up every increase in price.
//  5) If the price went down, we skip that day, because there's no profit in buying high and selling low.

class Solution {
    public int maxProfit(int[] prices) {
        int diff;
        int maxProfit = 0;

        for (int i = 1; i < prices.length; i++) {
            diff = prices[i] - prices[i - 1];
            if (diff > 0) maxProfit += diff;
        }

        return maxProfit;
    }
}