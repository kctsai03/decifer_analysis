import pandas as pd
from get_cn_clones import get_cn_clones
from mk_directed import mk_directed
from get_clone_trees import get_clone_trees
from map_single_clone_tree import map_single_clone_tree
from matplotlib import pyplot as plt
def plot_violation(best_input, clone_tree_index): 
    #figure out which clone trees violate the "coming out of nowhere" policy
    #(1, 0) --> (2, 1) can't happen
    #gives a dataframe with clone_tree, violating_edge, and violating_bin
    #
    #
    #
    #best_input is the tsv file of the input (with mutation bins and copy number clones)

    #create data frame for output
    df = pd.DataFrame(columns=['clone_tree', 'violating_edge', 'violating_bin'])


    all_clone_trees = mk_directed(get_clone_trees([0, 1, 2, 3]))


    old_bin_index = best_input.apply(lambda x: f'{x[0]}.{x[1]}.{x[2]}', axis = 1).tolist()
    bin_index = []
    for v in old_bin_index:
        if v not in bin_index:
            bin_index.append(v)
        # bin_index = ['1.1.26314488', '1.26314488.26644978', '1.26644978.40002884', ...
        # chr_num.start.end
    for curr in all_clone_trees:
        violated = False
        for bin in bin_index: #bin is 1.1.2631448
            inf = bin.split('.')
            chr_number = inf[0]
            start = inf[1]
            end = inf[2]
            chr_x = best_input[best_input['#CHR'] == int(chr_number)]
            row_number = chr_x[(chr_x['START'] == int(start)) & (chr_x['END'] == int(end))].index[0]
            cn_clones = get_cn_clones(best_input, row_number)
            mapped = map_single_clone_tree(curr, cn_clones)[0]
            for edge_index in range(len(mapped)):
                for i in range(2):
                    if mapped[edge_index][0][i] == '0' and mapped[edge_index][1][i] != '0':
                        df.loc[len(df.index)] = [curr, curr[edge_index], bin]
                        violated = True
                        break
    # get number of bins with violations for each clone tree and plot
    #
    #
    #
    #clone_tuple is a df of the violations as a tuple
    clone_tuple = df['clone_tree'].apply(lambda x: tuple(x))

    #ls is a series that gives me (clone tree) (number of times it violates a bin)
    ls = clone_tuple.value_counts()
    #clone_trees_tuple is a list of the (clone tree) as tuples
    #counts is a list of all the counts (number of times it violates a bin)
    clone_trees_tuple = list(ls.index)
    counts = list(ls)

    #dictionary with key:value as (clone tree number): (number of mutations)
    violation_counts = {}

    clone_trees_list = [list(ele) for ele in clone_trees_tuple]

    for x in range(len(all_clone_trees)):
        for i in range(len(clone_trees_list)):
            if clone_trees_list[i] == all_clone_trees[x]:
                violation_counts[x] = counts[i]
                break
            else:
                violation_counts[x] = 0

    #counts = list of the values of violation_counts = [0, 12, 12, 119, ...]
    #number of violations
    counts = violation_counts.values()
    # Creating histogram
    #clone_tree_index = [0, 1, 2, 3, .. 16] = x axis
    #counts = y axis
    plt.bar(clone_tree_index, counts, tick_label = clone_tree_index, color = 'black')
    plt.xlabel("Clone Tree Number")
    plt.ylabel("Number of bins that violate clone tree")
    plt.title("Violations for Clone Tree")
    plt.show()





