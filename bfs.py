import collections

def bfs(graph,root):
    visited = set()                               #visited  set
    queue = collections.deque([root])             #queue    dequeue  root ko queue
    visited.add(root)                             #visited  root ko add
    while queue:                                  #while queue
        vertex = queue.popleft()
        print(str(vertex) + " ", end="")
        for x in graph[vertex]:
            if x not in visited:
                visited.add(x)
                queue.append(x)

if __name__ == '__main__' :
    graph = {0: [1, 2], 1: [2], 2: [3], 3: [1, 2]}
    print("Following is Breadth First Traversal: ")
    bfs(graph,0)