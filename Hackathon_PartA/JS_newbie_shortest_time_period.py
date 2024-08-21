# import heapq
# import sys

# def dijkstra(adj, src, dest):
#     # Initialize distances with infinity
#     dist = {node: sys.maxsize for node in adj}
#     dist[src] = 0
    
#     # Min-heap priority queue
#     heap = [(0, src)]
    
#     while heap:
#         current_dist, u = heapq.heappop(heap)
        
#         # Skip if we have already found a better path
#         if current_dist > dist[u]:
#             continue
        
#         for v, weight in adj[u]:
#             if dist[v] > dist[u] + weight:
#                 dist[v] = dist[u] + weight
#                 heapq.heappush(heap, (dist[v], v))
    
#     return dist[dest] if dist[dest] != sys.maxsize else -1

# def main():
#     try:
#         # Read number of nodes
#         n = int(input().strip())
        
#         # Read node IDs
#         nodes = list(map(int, input().strip().split()))
#         if len(nodes) != n:
#             print("Error: Number of nodes does not match the provided node IDs.")
#             return
        
#         # Build adjacency list
#         adj = {node: [] for node in nodes}
        
#         # Read number of edges
#         e = int(input().strip())
        
#         # Read edges
#         for _ in range(e):
#             edge_input = input().strip().split()
#             if len(edge_input) != 3:
#                 print("Error: Each edge must have exactly 3 values (source, destination, weight).")
#                 return
#             x, y, d = map(int, edge_input)
#             if x not in adj or y not in adj:
#                 print(f"Error: Edge includes undefined node(s): {x}, {y}")
#                 return
#             adj[x].append((y, d))
        
#         # Read source and destination
#         src_dest = input().strip().split()
#         if len(src_dest) != 2:
#             print("Error: Source and destination input must have exactly 2 values.")
#             return
#         src, dest = map(int, src_dest)
#         if src not in adj or dest not in adj:
#             print(f"Error: Source or destination node not found in the graph: {src}, {dest}")
#             return
        
#         # Compute shortest path
#         result = dijkstra(adj, src, dest)
#         print(result)
    
#     except Exception as ex:
#         print(f"An error occurred: {ex}")

# if __name__ == "__main__":
#     main()
import heapq
import sys

def dijkstra(adj, src, dest):
    # Initialize distances with infinity
    dist = {node: sys.maxsize for node in adj}
    dist[src] = 0
    
    # Min-heap priority queue
    heap = [(0, src)]
    
    while heap:
        current_dist, u = heapq.heappop(heap)
        
        # Skip if we have already found a better path
        if current_dist > dist[u]:
            continue
        
        for v, weight in adj[u]:
            if dist[v] > dist[u] + weight:
                dist[v] = dist[u] + weight
                heapq.heappush(heap, (dist[v], v))
    
    return dist[dest] if dist[dest] != sys.maxsize else -1

def main():
    try:
        # Read number of nodes
        n = int(input().strip())
        
        # Initialize adjacency list
        adj = {}
        
        # Read node IDs
        for _ in range(n):
            node = int(input().strip())
            adj[node] = []
        
        # Read number of edges
        e = int(input().strip())
        
        # Read edges
        for _ in range(e):
            x, y, d = map(int, input().strip().split())
            adj[x].append((y, d))
        
        # Read source and destination
        src = int(input().strip())
        dest = int(input().strip())
        
        # Compute shortest path
        result = dijkstra(adj, src, dest)
        print(result)
    
    except Exception as ex:
        print(f"An error occurred: {ex}")

if __name__ == "__main__":
    main()
