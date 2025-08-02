class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        List<Integer>[] graph = new List[numCourses];
        for (int i = 0; i < numCourses; i++) graph[i] = new ArrayList<>();
        for (int[] edge : prerequisites) graph[edge[0]].add(edge[1]);

        int[] state = new int[numCourses]; // 0 = unvisited, 1 = visiting, 2 = visited

        // Perform DFS
        Deque<Integer> stack = new ArrayDeque<>();
        for (int i = 0; i < numCourses; i++) {
            if (state[i] != 0) continue;
            stack.push(i);

            while (!stack.isEmpty()) {
                int node = stack.peek();

                if (state[node] == 0) {
                    state[node] = 1; // mark as visiting
                    for (int neighbor : graph[node]) {
                        if (state[neighbor] == 1) return false; // cycle
                        if (state[neighbor] == 0) stack.push(neighbor);
                    }
                } else {
                    stack.pop();
                    state[node] = 2; // mark as visited
                }
            }
        }
        return true;
    }
}

// Recursive DFS implemented below
class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        List<Integer>[] graph = new List[numCourses];
        for (int i = 0; i < numCourses; i++) graph[i] = new ArrayList<>();
        for (int[] pre : prerequisites) {
            graph[pre[0]].add(pre[1]); // edge: course → prerequisite
        }

        int[] state = new int[numCourses]; // 0 = unvisited, 1 = visiting, 2 = visited

        for (int i = 0; i < numCourses; i++) {
            if (state[i] == 0 && hasCycle(graph, state, i)) return false;
        }

        return true;
    }

    private boolean hasCycle(List<Integer>[] graph, int[] state, int node) {
        state[node] = 1; // mark as visiting
        for (int neighbor : graph[node]) {
            if (state[neighbor] == 1) return true; // found a back edge
            if (state[neighbor] == 0 && hasCycle(graph, state, neighbor)) return true;
        }
        state[node] = 2; // mark as fully visited
        return false;
    }
}