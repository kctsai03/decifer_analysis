# remove all duplicate paths for a single tree


def rm_duplicates(state_tree):
  for edge in state_tree:
    if edge[0] == edge[1]:
      state_tree.remove(edge)
