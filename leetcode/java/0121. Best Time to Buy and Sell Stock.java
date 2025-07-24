class Solution {
    public int maxProfit(int[] prices) {
        int minPrice = prices[0];
        int maxProfit = 0;

        for (int price: prices) {
            // Update minPrice if a new lower price is found
            minPrice = Math.min(minPrice, price);
            
            // Calculate and update maxProfit
            maxProfit = Math.max(maxProfit, price - minPrice);
        }

        return maxProfit;
    }
}