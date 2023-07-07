# checks if a clone tree is the same as the state tree

def is_valid_tree(clone_tree, state_tree):
  return sorted(clone_tree) == sorted(state_tree)

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