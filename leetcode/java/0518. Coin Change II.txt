class Solution {
    public int change(int amount, int[] coins) {
        int[] ways = new int[amount+1];
        ways[0] = 1;
        for(int coin:coins){
            //More optimized, due to 'i=coin' there is no need for if(i>=coin) check.
            for(int i=coin;i<ways.length;i++){
                ways[i] += ways[i-coin];
            }
        }
        return ways[amount];
    }
}

OR

class Solution {
    public int change(int amount, int[] coins) {
        int[] ways = new int[amount+1];
        ways[0] = 1;
        for(int coin:coins){
            for(int i=1;i<ways.length;i++){
                if(i>=coin) ways[i] += ways[i-coin];
            }
        }
        return ways[amount];
    }
}