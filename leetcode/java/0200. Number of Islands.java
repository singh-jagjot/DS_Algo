class Solution {
    public int numIslands(char[][] grid) {
        int totalIslands = 0;
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[i].length; j++) {
                if (grid[i][j] == '1') {
                    dfs(grid, i, j);
                    totalIslands++;
                }
            }
        }
        return totalIslands;
    }

    int[] dr = new int[]{0, 0, -1, 1};
    int[] dc = new int[]{-1, 1, 0, 0};

    void dfs(char[][] grid, int r, int c) {
        int m = grid.length;
        int n = grid[0].length;

        Deque<int[]> stack = new ArrayDeque<>();
        stack.push(new int[]{r, c});

        while (!stack.isEmpty()) {
            int[] node = stack.pop();
            int cr = node[0]; int cc = node[1];
            grid[cr][cc] = 'v';

            for (int d = 0; d < 4; d++) {
                int nr = cr + dr[d];
                int nc = cc + dc[d];
                if (nr >= 0 && nr < m && nc >= 0 && nc < n) {
                    if (grid[nr][nc] == '1') stack.push(new int[]{nr, nc});
                }
            }
        }
    }

    // For study below is recursive DFS (Above recommended)

    void dfs(char[][] grid, int r, int c) {
        if (r < 0 || r >= grid.length || c < 0 || c >= grid[0].length || grid[r][c] != '1') return;

        grid[r][c] = 'v';

        dfs(grid, r + 1, c);
        dfs(grid, r - 1, c);
        dfs(grid, r, c + 1);
        dfs(grid, r, c - 1);
    }
}

// Union-Find Approach
class Solution {
    public int numIslands(char[][] grid) {
        int rows = grid.length;
        int cols = grid[0].length;

        UnionFind uf = new UnionFind(grid);

        int[][] directions = {{0, 1}, {1, 0}, {-1, 0}, {0, -1}};
        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                if (grid[r][c] == '1') {
                    for (int[] d : directions) {
                        int nr = r + d[0], nc = c + d[1];
                        if (nr >= 0 && nr < rows && nc >= 0 && nc < cols && grid[nr][nc] == '1') {

                            //We're converting a 2D grid coordinate (row, col) into a 1D index using the formula:
                            //id = row * number_of_columns + column
                            //Union-Find is typically implemented as a 1D array, so for a 2D grid (m x n),
                            //each cell at (r, c) is uniquely mapped to an index:
                            //index = r * n + c

                            uf.union(r * cols + c, nr * cols + nc);
                        }
                    }
                }
            }
        }

        return uf.getCount();
    }
}

// 🧱 Union-Find class with path compression and union by rank
class UnionFind {
    int[] parent;
    int[] rank;
    int count; // number of islands

    public UnionFind(char[][] grid) {
        int m = grid.length;
        int n = grid[0].length;
        parent = new int[m * n];
        rank = new int[m * n];
        count = 0;

        // Initialize each cell: if it's land ('1'), make it its own parent
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == '1') {
                    int id = i * n + j;
                    parent[id] = id;
                    count++;
                }
            }
        }
    }

    public int find(int x) {
        if (parent[x] != x) {
            parent[x] = find(parent[x]); // path compression
        }
        return parent[x];
    }

    public void union(int x, int y) {
        int xr = find(x);
        int yr = find(y);
        if (xr == yr) return;

        // union by rank
        if (rank[xr] < rank[yr]) {
            parent[xr] = yr;
        } else if (rank[xr] > rank[yr]) {
            parent[yr] = xr;
        } else {
            parent[yr] = xr;
            rank[xr]++;
        }
        count--; // two islands merged into one
    }

    public int getCount() {
        return count;
    }
}
