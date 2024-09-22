class Solution {
    //Recursive
    // public int uniquePaths(int m, int n) {
    //     return getWays(0,0,m,n,new int[m][n]);
    // }
    // int getWays(int i, int j, int m, int n, int[][] a){

    //     if(i==m-1||j==n-1) return 1;
    //     //Commenting above line and uncommenting below two lines will also work
    //     // if (i > m - 1 || j > n - 1) return 0;
    //     // if (i == m - 1 && j == n - 1) return 1;
    //     if(a[i][j]>0) return a[i][j];
    //     a[i][j] = getWays(i+1,j,m,n,a)+getWays(i,j+1,m,n,a);
    //     return a[i][j];
    // }

    //Iterative
    // public int uniquePaths(int m, int n) {
    //     int[][] paths = new int[m][n];
    //     for (int i = 0; i < m; i++) {
    //         paths[i][0] = 1;
    //     }
    //     for (int i = 0; i < n; i++) {
    //         paths[0][i] = 1;
    //     }
    //     for (int i = 1; i < m; i++) {
    //         for (int j = 1; j < n; j++) {
    //             paths[i][j]=paths[i-1][j]+paths[i][j-1];
    //         }
    //     }
    //     return paths[m-1][n-1];
    // }

    // Best Solution(We only need to store top row)
    // Time O(m*n), Space O(n)
    public int uniquePaths(int m, int n) {
        int[] top = new int[n];
        Arrays.fill(top, 1);
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                top[j] += top[j-1];
            }
        }
        return top[n-1];
    }
    
}