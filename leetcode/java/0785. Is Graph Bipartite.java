class Solution {
    public boolean isBipartite(int[][] graph) {
        int[] visited = new int[graph.length];
        int[] partition = new int[graph.length];

        Deque<Integer> stack = new ArrayDeque<>();
        for (int i = 0; i < graph.length; i++) {
            if(visited[i]==0){
                partition[i] = 1;
                stack.push(i);
            }
            while (!stack.isEmpty()) {
                int node = stack.peek();
                if(visited[node] == 0) visited[node] = 1;
                //    System.out.print(node + "->");
                boolean neighboursVisited = true;
                for(int neighbour: graph[node]){
                    if(visited[neighbour] == 0) {
                        stack.push(neighbour);
                        neighboursVisited = false;
                        if(partition[node] == 1) partition[neighbour] = 2;
                        else partition[neighbour] = 1;
                        break;
                    }
                    if(partition[node] == partition[neighbour]) return false;

                }
                if(neighboursVisited) {
                    visited[node] = 2;
                    stack.pop();
                    System.out.println();
                }
            }
        }
        // for (int p: partition){
        //     System.out.print(p + ",");
        // }
        // System.out.println();
        // for (int v: visited){
        //     System.out.print(v + ",");
        // }
        return true;
    }
}