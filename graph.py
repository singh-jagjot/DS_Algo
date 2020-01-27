from typing import List

nodes = int(input())
edges = int(input())

# Using Adjacency List implementation.
# Initializing empty graph acc to number of nodes.
graph = [[] for x in range(nodes)]


# Basic DFS implementation.
def dfs(node: int, graph: List[List], trace: List):
    trace[node] = 1
    print("->", node, end=" ")
    for x in graph[node]:
        if trace[x] != 1:
            dfs(x, graph, trace)


# Storing edges.
for x in range(edges):
    n1, n2 = list(map(int, input().split()))
    graph[n1].append(n2)
    graph[n2].append(n1)

# Printing Adjacency List.
for i, x in enumerate(graph):
    print(i, x)

# Creating trace list to mark visited nodes for DFS.
trace = [0] * nodes

# Printing DFS order.
print("DFS: ", end="")
dfs(0, graph, trace)
