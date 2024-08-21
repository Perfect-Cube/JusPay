from collections import defaultdict

def dfs(node, parent, graph, visited, dirty):
    visited[node] = True
    
    for child in graph[node]:
        if not visited[child]:
            dfs(child, node, graph, visited, dirty)
    
    if parent != -1:
        dirty[parent] = dirty[parent] or dirty[node]

def main():
    n = int(input().strip())
    nodes = [int(input().strip()) for _ in range(n)]
    
    sz = max(nodes) + 1

    edges = int(input().strip())
    graph = defaultdict(list)
    visited = [False] * sz
    dirty = [False] * sz
    
    for _ in range(edges):
        u, v = map(int, input().strip().split())
        graph[v].append(u)
    
    enemy = int(input().strip())
    person = int(input().strip())

    dirty[enemy] = True
    
    dfs(person, -1, graph, visited, dirty)
    
    result = []
    for child in graph[person]:
        if dirty[child]:
            result.append(child)
    
    print(" ".join(map(str, result)))

if __name__ == "__main__":
    main()
