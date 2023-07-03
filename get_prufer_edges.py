#input is the prufer sequence (in our case, just two numbers)
#output is the list of edges of the corresponding tree
#ex. input [0, 1]
#ex. output [0, 2], [0, 1], [1, 3]


def get_prufer_edges(prufer_sequence):
  num_vertices = 4

  # create the list array (all the values of the vertices)
  all_nodes = [0, 1, 2, 3]

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

