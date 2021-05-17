# -*- coding: utf-8 -*-
graph_list = {1: set([3, 4]),
              2: set([3, 4, 5]),
              3: set([1, 5]),
              4: set([1]),
              5: set([2, 6]),
              6: set([3, 5])}
root_node = 1

def DFS_with_adj_list(graph, root):
    visited = []
    stack = [root]

    while stack:
        print("Stack : ", stack)
        print("Visited : ", visited)
        n = stack.pop()
        print("n : ", n)
        if n not in visited:
            visited.append(n)
            stack += graph[n] - set(visited)
    return visited

print(DFS_with_adj_list(graph_list, root_node))




