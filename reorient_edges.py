from collections import deque

def reorient_edges(edges):
    adj_list = {}  # Adjacency list to store the undirected tree

    # Step 1: Create adjacency list representation
    for u, v in edges:
        if u not in adj_list:
            adj_list[u] = []
        if v not in adj_list:
            adj_list[v] = []
        adj_list[u].append(v)
        adj_list[v].append(u)

    directed_edges = []  # List to store the directed edges
    visited = set()  # Set to keep track of visited nodes during BFS

    # Step 2: Perform BFS to assign directions and determine parent-child relationships
    queue = deque([(0, -1)])  # Start BFS from node 0 with parent -1

    while queue:
        node, parent = queue.popleft()
        visited.add(node)

        for neighbor in adj_list[node]:
            if neighbor != parent:  # Exclude the parent node
                if node not in directed_edges:
                    directed_edges.append((node, neighbor))
                queue.append((neighbor, node))

    return directed_edges
