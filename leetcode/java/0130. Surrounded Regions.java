class Solution {
    public void solve(char[][] board) {
        int rows = board.length;
        int cols = board[0].length;

        // Step 1: Start dfs from border 'O's
        for (int i = 0; i < rows; i++) {
            if (board[i][0] == 'O')
                dfs(board, i, 0);
            if (board[i][cols - 1] == 'O')
                dfs(board, i, cols - 1);
        }
        for (int i = 0; i < cols; i++) {
            if (board[0][i] == 'O')
                dfs(board, 0, i);
            if (board[rows - 1][i] == 'O')
                dfs(board, rows - 1, i);
        }

        // Step 2: Flipping safe 'S's back to 'O' and remaing 'O's to 'X's
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (board[i][j] == 'S')
                    board[i][j] = 'O';
                else if (board[i][j] == 'O')
                    board[i][j] = 'X';
            }
        }

        // for (char[] cs : board) {
        // System.out.println(cs);
        // }
    }

    void dfs(char[][] board, int row, int col) {
        Deque<int[]> stack = new ArrayDeque<>();
        stack.push(new int[] { row, col });

        while (!stack.isEmpty()) {
            var curr = stack.pop();
            int r = curr[0], c = curr[1];
            // Marking S for safe
            board[r][c] = 'S';
            for (var neighbour : getNeighbours(board, r, c)) {
                int nr = neighbour[0], nc = neighbour[1];
                if (board[nr][nc] == 'O')
                    stack.push(neighbour);
            }

            // We can uncomment below code to get rid of getNeighbours(), logic is same. This gives better performance.
            // int[] dr = {-1, 0, 1, 0}, dc = {0, 1, 0, -1};
            // for (int d = 0; d < 4; d++) {
            //     int nr = r + dr[d], nc = c + dc[d];
            //     if (nr >= 0 && nr < board.length && nc >= 0 && nc < board[0].length && board[nr][nc] == 'O')
            //         stack.push(new int[]{nr, nc});
            // }
        }
    }

    List<int[]> getNeighbours(char[][] board, int row, int col) {
        List<int[]> neighbours = new ArrayList<>();
        int rows = board.length;
        int cols = board[0].length;
        // Up
        if (row - 1 >= 0)
            neighbours.add(new int[] { row - 1, col });
        // Down
        if (row + 1 <= rows - 1)
            neighbours.add(new int[] { row + 1, col });
        // Left
        if (col - 1 >= 0)
            neighbours.add(new int[] { row, col - 1 });
        // Right
        if (col + 1 <= cols - 1)
            neighbours.add(new int[] { row, col + 1 });

        return neighbours;
    }
}