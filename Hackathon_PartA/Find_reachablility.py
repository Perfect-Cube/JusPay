def dfs(graph, visited, node):
    visited[node] = True
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(graph, visited, neighbor)

def main():
    n = int(input())
    node_index = {}
    nodes = []

    for i in range(n):
        node = int(input())
        nodes.append(node)
        node_index[node] = i

    q = int(input())
    graph = [[] for _ in range(n)]

    for _ in range(q):
        u, v = map(int, input().split())
        if u in node_index and v in node_index:
            graph[node_index[u]].append(node_index[v])
            # Uncomment the following line if the graph is undirected
            # graph[node_index[v]].append(node_index[u])

    start_node, end_node = map(int, input().split())

    if start_node not in node_index or end_node not in node_index:
        print(0)
        return

    start_index = node_index[start_node]
    end_index = node_index[end_node]

    visited = [False] * n
    dfs(graph, visited, start_index)

    if visited[end_index]:
        print(1)
    else:
        print(0)

if __name__ == "__main__":
    main()
