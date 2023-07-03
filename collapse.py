#input is a state tree
#output is a state tree that doesn't have any of the same edges written twice

def collapse(tree):
  parallel = []
  for edge in tree:
    if edge not in parallel:
      parallel.append(edge)
  return parallel
