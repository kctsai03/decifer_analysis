#converts a single clone tree to the state tree
def map_single_clone_tree(clone_tree, cn_clones):
  output = []
  updated_tree = []
  for edge in clone_tree:
    updated_edge = []
    for i in range(2):
      updated_edge.append(cn_clones[edge[i]])
    updated_tree.append(updated_edge)
  output.append(updated_tree)
  return output