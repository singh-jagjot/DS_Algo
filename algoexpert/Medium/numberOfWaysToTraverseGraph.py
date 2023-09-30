# O(n*m) time | O(n*m) space
# def numberOfWaysToTraverseGraph(width, height):
#     # Write your code here.
#     graph = [[0 for _ in range(width)] for _ in range(height)]

#     for w in range(height):
#         for h in range(width):
#             if w == 0 or h == 0:
#                 graph[w][h] = 1
#             else:
#                 graph[w][h] = graph[w - 1][h] + graph[w][h - 1]
#     return graph[-1][-1]

import math
# O(n+m) time | O(1) space
def numberOfWaysToTraverseGraph(width, height):
    width -= 1
    height -= 1
    return math.factorial(width + height) / (math.factorial(width) * math.factorial(height))
