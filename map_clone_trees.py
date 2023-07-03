#converts all clone tree to the state tree
def map_clone_trees(all_clone_trees, cn_clones):
  output = []
  for tree in all_clone_trees:
    updated_tree = []
    for edge in tree:
      updated_edge = []
      for i in range(2):
        updated_edge.append(cn_clones[edge[i]])
      updated_tree.append(updated_edge)
    output.append(updated_tree)
  return output
