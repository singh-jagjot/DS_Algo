// Using BFS Coloring
class Solution {
    public boolean isBipartite(int[][] graph) {
        int[] color = new int[graph.length]; // 0 = uncolored, 1/2 = partitions

        for (int i = 0; i < graph.length; i++) {
            if (color[i] != 0) continue;

            Queue<Integer> queue = new ArrayDeque<>();
            queue.offer(i);
            color[i] = 1;

            while (!queue.isEmpty()) {
                int node = queue.poll();
                for (int neighbor : graph[node]) {
                    if (color[neighbor] == 0) {
                        color[neighbor] = 3 - color[node]; // flip between 1 and 2
                        queue.offer(neighbor);
                    } else if (color[neighbor] == color[node]) {
                        return false; // same color on both ends → not bipartite
                    }
                }
            }
        }

        return true;
    }
}

// Using Iterative DFS Coloring
class Solution {
    public boolean isBipartite(int[][] graph) {
        int[] color = new int[graph.length]; // 0 = unvisited, 1 = red, -1 = blue

        for (int i = 0; i < graph.length; i++) {
            if (color[i] != 0) continue;

            Deque<Integer> stack = new ArrayDeque<>();
            stack.push(i);
            color[i] = 1;

            while (!stack.isEmpty()) {
                int node = stack.pop();
                for (int neighbor : graph[node]) {
                    if (color[neighbor] == 0) {
                        color[neighbor] = -color[node]; // assign opposite color
                        stack.push(neighbor);
                    } else if (color[neighbor] == color[node]) {
                        return false; // same color conflict
                    }
                }
            }
        }
        return true;
    }
}
