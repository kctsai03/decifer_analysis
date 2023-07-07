#input is a state tree
#output is a state tree that doesn't have any of the same edges written twice

def collapse(tree):
  parallel = []
  for edge in tree:
    if edge not in parallel:
      parallel.append(edge)
  return parallel

# remove all duplicate paths for a single tree

def rm_duplicates(state_tree):
  for edge in state_tree:
    if edge[0] == edge[1]:
      state_tree.remove(edge)
