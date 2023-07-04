# checks if a clone tree is the same as the state tree

def is_valid_tree(clone_tree, state_tree):
  #test 3
  return sorted(clone_tree) == sorted(state_tree)


