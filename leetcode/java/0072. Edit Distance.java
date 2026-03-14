//Time: O(N×M) Space: O(min(N,M))
class Solution {
    public int minDistance(String word1, String word2) {
        int n = word1.length();
        int m = word2.length();

        // Always use the smaller string for the array to ensure O(min(N, M)) space
        if (n < m) return minDistance(word2, word1);

        // dp[j] will store the edit distance for word1[0...i] and word2[0...j]
        int[] dp = new int[m + 1];

        // Base case: transforming word1 (empty) to word2[0...j] requires j insertions
        for (int j = 0; j <= m; j++) {
            dp[j] = j;
        }

        for (int i = 1; i <= n; i++) {
            int prevDiag = dp[0]; // Stores dp[i-1][j-1]
            dp[0] = i; // Base case: transforming word1[0...i] to word2 (empty)

            for (int j = 1; j <= m; j++) {
                int temp = dp[j]; // Save the current value before it's overwritten

                if (word1.charAt(i - 1) == word2.charAt(j - 1)) {
                    // Characters match: no new operation needed
                    dp[j] = prevDiag;
                } else {
                    // Characters differ: 1 + min(Replace, Insert, Delete)
                    // Replace: prevDiag | Insert: dp[j-1] | Delete: dp[j]
                    dp[j] = 1 + Math.min(prevDiag, Math.min(dp[j - 1], dp[j]));
                }
                prevDiag = temp; // Update prevDiag for the next iteration (j+1)
            }
        }
        return dp[m];
    }
}

//My solution. Use the solution above instead, it's better and clean.
class Solution {
    public int minDistance(String word1, String word2) {
        String big, small;
        if(word1.length()>word2.length()){
            big=word1;
            small=word2;
        }else if(word2.length()>word1.length()){
            big=word2;
            small=word1;
        }else{
            big=word1;
            small=word2;
        }
        int [] pre = new int[1+small.length()];
        int [] curr = new int[1+small.length()];

        for (int i=0;i<pre.length;i++){
            pre[i]=i;
        }
        for(int i=0;i<big.length();i++){
            curr[0]=i+1;
            for(int j=0;j<small.length();j++){
                if(big.charAt(i)==small.charAt(j)){
                    curr[j+1]=pre[j];
                }else{
                    curr[j+1]=1+Math.min(curr[j], Math.min(pre[j], pre[j+1]));
                }
            }
            for(int j=0;j<curr.length;j++) pre[j]=curr[j];
        }
        return curr[curr.length-1];
    }
}