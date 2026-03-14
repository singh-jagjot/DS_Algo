//Time: O(N×M) Space: O(min(N,M))
class Solution {
    public int longestCommonSubsequence(String text1, String text2) {
        int n = text1.length();
        int m = text2.length();

        // Optimization: Ensure text2 is the shorter string to minimize space
        if (n < m) return longestCommonSubsequence(text2, text1);

        // Micro-optimization: Convert to char array to avoid charAt() overhead
        char[] s1 = text1.toCharArray();
        char[] s2 = text2.toCharArray();

        // dp[j] stores the LCS length for s1[0...i-1] and s2[0...j-1]
        int[] dp = new int[m + 1];

        for (int i = 1; i <= n; i++) {
            // prevDiag represents the top-left neighbor in the DP matrix (dp[i-1][j-1])
            int prevDiag = 0;
            for (int j = 1; j <= m; j++) {
                // Store current dp[j] (which is dp[i-1][j]) before it gets updated to dp[i][j]
                int temp = dp[j];

                if (s1[i - 1] == s2[j - 1]) {
                    // If characters match, add 1 to the LCS of the prefixes (diagonal move)
                    dp[j] = prevDiag + 1;
                } else {
                    // If they don't match, take the max LCS by either:
                    // 1. Excluding current s1 char (dp[j])
                    // 2. Excluding current s2 char (dp[j-1])
                    dp[j] = Math.max(dp[j], dp[j - 1]);
                }
                // The old dp[j] becomes the prevDiag for the next iteration (j+1)
                prevDiag = temp;
            }
        }
        return dp[m];
    }
}

//My Solution
//Time: O(N×M) Space: O(min(N,M))
class Solution {
    public int longestCommonSubsequence(String text1, String text2) {
        int n = text1.length();
        int m = text2.length();
        if(n<m) return longestCommonSubsequence(text2, text1);
        n++;
        int[] dp = new int[++m];
        for (int i = 0; i < m; i++) {
            dp[i] = 0;
        }

        for (int i = 1; i < n; i++) {
            int prevDia = dp[0];
            for (int j = 1; j < m; j++) {
                int temp = dp[j];
                if(text1.charAt(i-1) == text2.charAt(j-1)) {
                    dp[j] = prevDia + 1;
                } else {
                    dp[j] = Math.max(dp[j-1], dp[j]);
                }
                prevDia = temp;
            }
        }
        return dp[m-1];
    }
}

//My Solution
//Time: O(N×M) Space: O(N*M)
class Solution {
    public int longestCommonSubsequence(String text1, String text2) {
        int n = text1.length()+1;
        int m = text2.length()+1;

        int[][] grid = new int[n][m];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                grid[i][j] = 0;
            }
        }

        for (int i = 1; i < n; i++) {
            char text1Char = text1.charAt(i-1);
            for (int j = 1; j < m; j++) {
                char text2Char = text2.charAt(j-1);
                if(text1Char == text2Char) {
                    grid[i][j] = grid[i-1][j-1] + 1;
                } else {
                    grid[i][j] = Math.max(grid[i][j-1], grid[i-1][j]);
                }
            }
        }
        return grid[n-1][m-1];
    }
}