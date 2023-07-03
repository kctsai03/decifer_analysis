#get copy number clones into a dictionary
#input: best.seg.ucn.txv
#row number
#output:
#{0: ['1', '1'], 1: ['2', '2'], 2: ['4', '0'], 3: ['4', '0']}

def get_cn_clones(best_input, row_number):
  #cn_clones is a dictionary with key: value pairs as the clone number: the allele specific copy numbers
  cn_clones = {0: best_input.iloc[row_number]['cn_normal'], 1: best_input.iloc[row_number]['cn_clone1'], 2: best_input.iloc[row_number]['cn_clone2'], 3: best_input.iloc[row_number]['cn_clone3']}

  for key in cn_clones:
    split = cn_clones[key].split("|")
    cn_clones[key] = []
    cn_clones[key].append(split[0])
    cn_clones[key].append(split[1])
  return cn_clones