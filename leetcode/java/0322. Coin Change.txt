class Solution {
    public int coinChange(int[] coins, int amount) {
        int[] minCoins = new int[amount+1];
        Arrays.fill(minCoins, amount+1);
        minCoins[0]=0;
        for(int coin:coins){
            for(int i=coin;i<minCoins.length;i++){
                minCoins[i]=Math.min(minCoins[i],1+minCoins[i-coin]);
            }
        }
        return minCoins[amount]>amount?-1:minCoins[amount];
    }
}