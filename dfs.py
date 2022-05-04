def dfs(graph, root, visited=None):
    if visited is None:
        visited = set()
    visited.add(root)
    print(root)
    for x in graph[root] - visited:
        dfs(graph, x, visited)
    return visited

graph = {'0': set(['1', '2']),
         '1': set(['0', '3', '4']),
         '2': set(['0']),
         '3': set(['1']),
         '4': set(['2', '3'])}

dfs(graph,'0')