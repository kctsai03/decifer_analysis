#makes the edges of an undirected tree a directed tree with root = 0
from reorient_edges import reorient_edges

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
