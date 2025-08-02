class Solution {
    public int orangesRotting(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;

        Deque<int[]> queue = new ArrayDeque<>();

        // Add all initially rotten oranges to queue
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 2)
                    queue.offerLast(new int[]{i, j});
            }
        }

        // Directions: up, down, left, right
        int[] dr = {-1, 1, 0, 0};
        int[] dc = {0, 0, -1, 1};

        int minutes = -1;
        // Start from -1 because the first level (initial rotten oranges) is "minute 0"
        // We only increment minutes *after* spreading rot, so the initial minute is counted as 0 after first pass.

        // Performing BFS
        while (!queue.isEmpty()) {
            int size = queue.size(); // current level (minute)

            for (int i = 0; i < size; i++) {
                int[] cell = queue.removeFirst();

                for (int d = 0; d < 4; d++) {
                    int nr = cell[0] + dr[d];
                    int nc = cell[1] + dc[d];

                    // Check bounds and if the neighbor is a fresh orange
                    if (nr >= 0 && nr < m && nc >= 0 && nc < n && grid[nr][nc] == 1) {
                        grid[nr][nc] = 2; // mark as rotten
                        queue.offerLast(new int[]{nr, nc});
                    }
                }
            }
            minutes++; // completed one minute of rotting
        }

        // Check if any fresh oranges are left
        for (int[] row : grid) {
            for (int val : row) {
                if (val == 1)
                    return -1;
            }
        }

        // If no rotting was needed (i.e., no fresh oranges), return 0 instead of -1
        return Math.max(minutes, 0);
    }
}
