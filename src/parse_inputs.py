#parse state tree data from file
#input:
#(1,1,0)->(1,1,1);(1,1,0)->(2,2,0);(1,1,0)->(4,0,0)
#output:
#[[['1', '1'], ['1', '1']], [['1', '1'], ['2', '2']], [['1', '1'], ['4', '0']]]
from collapse import rm_duplicates

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
#get copy number clones into a dictionary
#input: best.seg.ucn.txv
#row number
#output:
#{0: ['1', '1'], 1: ['2', '2'], 2: ['4', '0'], 3: ['4', '0']}

def get_cn_clones(best_input, row_number):
  #cn_clones is a dictionary with key: value pairs as the clone number: the allele specific copy numbers
  cn_clones = {0: best_input.iloc[row_number]['cn_normal']}
  for col in best_input.columns:
    if 'cn_clone' in col:
      s = int(col.replace('cn_clone', ''))
      cn_clones[s] = best_input.iloc[row_number][col]

  for key in cn_clones:
    split = cn_clones[key].split("|")
    cn_clones[key] = []
    cn_clones[key].append(split[0])
    cn_clones[key].append(split[1])
  return cn_clones