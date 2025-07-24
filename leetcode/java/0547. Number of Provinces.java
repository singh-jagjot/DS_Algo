// Can also be solved by DFS

class UnionFind<T> {
    Map<T, T> parents = new HashMap<>();
    Map<T, Integer> rank = new HashMap<>();
    int componentCount = 0; // Tracks the number of disjoint sets

    // Adds a new element as its own component (if not already present)
    void makeSet(T val) {
        if (!parents.containsKey(val)) {
            parents.put(val, val);
            rank.put(val, 0);
            componentCount++;
        }
    }

    // Finds root with path compression
    T find(T val) {
        if (!parents.containsKey(val)) return null;
        T parent = parents.get(val);
        if (!val.equals(parent)) {
            parents.put(val, find(parent));
        }
        return parents.get(val);
    }

    // Unions two components if they are disjoint
    void union(T val1, T val2) {
        T root1 = find(val1);
        T root2 = find(val2);

        // Skip if any value not found or already in same component
        if (root1 == null || root2 == null || root1.equals(root2)) return;

        // Union by rank optimization
        if (rank.get(root1) < rank.get(root2)) {
            parents.put(root1, root2);
        } else if (rank.get(root1) > rank.get(root2)) {
            parents.put(root2, root1);
        } else {
            parents.put(root2, root1);
            rank.put(root1, rank.get(root1) + 1);
        }

        componentCount--; // Successful merge reduces component count
    }

    // True if both values belong to the same component
    boolean isConnected(T val1, T val2) {
        T root1 = find(val1);
        T root2 = find(val2);
        return root1 != null && root1.equals(root2);
    }

    // Returns current number of connected components
    int getComponentCount() {
        return componentCount;
    }

    // Returns all components as root ? set of nodes
    Map<T, Set<T>> getComponents() {
        Map<T, Set<T>> components = new HashMap<>();
        for (T node : parents.keySet()) {
            T root = find(node); // ensures path compression
            components.computeIfAbsent(root, k -> new HashSet<>()).add(node);
        }
        return components;
    }
}

class Solution {
    public int findCircleNum(int[][] isConnected) {
        UnionFind<Integer> uf = new UnionFind<>();
        int n = isConnected.length;

        for (int i = 0; i < n; i++) {
            uf.makeSet(i);
        }

        // Avoid redundant unions by only traversing upper triangle
        // as isConnected[][] is symmetric
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                if (isConnected[i][j] == 1) {
                    uf.union(i, j);
                }
            }
        }

        return uf.getComponentCount();
    }
}

//  OR MY SOLUTION BELOW (Above recommended)

class UnionFind<T> {
    Map<T, T> parents = new HashMap<>();
    Map<T, Integer> rank = new HashMap<>();
    int componentCount = 0; // Tracks the number of disjoint sets

    // Adds a new element as its own component (if not already present)
    void makeSet(T val) {
        if (!parents.containsKey(val)) {
            parents.put(val, val);
            rank.put(val, 0);
            componentCount++;
        }
    }

    // Finds root with path compression
    T find(T val) {
        if (!parents.containsKey(val)) return null;
        T parent = parents.get(val);
        if (!val.equals(parent)) {
            parents.put(val, find(parent));
        }
        return parents.get(val);
    }

    // Unions two components if they are disjoint
    void union(T val1, T val2) {
        T root1 = find(val1);
        T root2 = find(val2);

        // Skip if any value not found or already in same component
        if (root1 == null || root2 == null || root1.equals(root2)) return;

        // Union by rank optimization
        if (rank.get(root1) < rank.get(root2)) {
            parents.put(root1, root2);
        } else if (rank.get(root1) > rank.get(root2)) {
            parents.put(root2, root1);
        } else {
            parents.put(root2, root1);
            rank.put(root1, rank.get(root1) + 1);
        }

        componentCount--; // Successful merge reduces component count
    }

    // True if both values belong to the same component
    boolean isConnected(T val1, T val2) {
        T root1 = find(val1);
        T root2 = find(val2);
        return root1 != null && root1.equals(root2);
    }

    // Returns current number of connected components
    int getComponentCount() {
        return componentCount;
    }

    // Returns all components as root ? set of nodes
    Map<T, Set<T>> getComponents() {
        Map<T, Set<T>> components = new HashMap<>();
        for (T node : parents.keySet()) {
            T root = find(node); // ensures path compression
            components.computeIfAbsent(root, k -> new HashSet<>()).add(node);
        }
        return components;
    }
}

class Solution {
    public int findCircleNum(int[][] isConnected) {
        UnionFind<Integer> uf = new UnionFind<>();

        for (int i = 0; i < isConnected.length; i++) {
            uf.makeSet(i);
        }

        for (int i = 0; i < isConnected.length; i++) {
            for (int j = 0; j < isConnected.length; j++) {
                if(isConnected[i][j]==1){
                    uf.union(i, j);
                }
            }
        }
        
        return uf.getComponentCount();
    }
}