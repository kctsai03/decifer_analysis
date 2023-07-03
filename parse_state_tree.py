#parse state tree data from file
#input:
#(1,1,0)->(1,1,1);(1,1,0)->(2,2,0);(1,1,0)->(4,0,0)
#output:
#[[['1', '1'], ['1', '1']], [['1', '1'], ['2', '2']], [['1', '1'], ['4', '0']]]
from rm_duplicates import rm_duplicates

def parse_state_tree(state_tree_raw):
  state_tree_list = state_tree_raw.split(";")
  state_tree = []
  for i in state_tree_list:
    edge = i.split('->')

    edge_start = []
    edge_start.append(edge[0].split(',')[0][1])
    edge_start.append(edge[0].split(',')[1])

    edge_end = []
    edge_end.append(edge[1].split(',')[0][1])
    edge_end.append(edge[1].split(',')[1])

    edge_update = []
    edge_update.append(edge_start)
    edge_update.append(edge_end)

    state_tree.append(edge_update)
  rm_duplicates(state_tree)
  return state_tree
