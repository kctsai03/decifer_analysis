from collections import deque

#takes in an array and gets all the possible clone trees edge list
#input is [0, 1, 2, 3]
#output is [0, 2], [0, 1], [1, 3]
#[0, 1], [0, 2], [0, 3] etc.
def get_clone_trees(vertices):
  output = []
  for i in vertices:
    for j in vertices:
      prufer_sequence = [i, j]
      edges = get_prufer_edges(prufer_sequence, len(vertices))
      output.append(edges)
  return output

#input is the prufer sequence (in our case, just two numbers)
#output is the list of edges of the corresponding tree
#ex. input [0, 1]
#ex. output [0, 2], [0, 1], [1, 3]


def get_prufer_edges(prufer_sequence, num_vertices):

  # create the list array (all the values of the vertices)
  all_nodes = list(range(num_vertices))

  edge_list = []

  # we need to find the smallest element in the list that isn't in the sequence
  for index in range(2):
    for node in all_nodes:
      if node not in prufer_sequence:
        edge_list.append([prufer_sequence[index], node])
        prufer_sequence[index] = -1
        all_nodes.remove(node)
        break
  edge_list.append([all_nodes[0], all_nodes[1]])
  return edge_list


#makes the edges of an undirected tree a directed tree with root = 0

def mk_directed(all_clone_trees):
  output = []
  for tree in all_clone_trees:
    for edge in tree:
      if edge[1] == 0:
        all_clone_trees[all_clone_trees.index(tree)][tree.index(edge)] = [0, edge[0]]
  for tree in all_clone_trees:
    tree = reorient_edges(tree)
    output.append(tree)
  return output




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
