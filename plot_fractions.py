#takes the files of the valid clone trees and the existing mutation files and
#only keeps the mutations in both
#then plots a graph showing the fraction of mutations where each clone tree
#is valid
#
#
#
#df_clone_trees is the valid clone trees file as a dataframe
from mk_directed import mk_directed
from get_clone_trees import get_clone_trees
from matplotlib import pyplot as plt
def plot_fractions(df_clone_trees, df_vcf, clone_tree_index):


    #list of all the clone trees
    clone_tree_list = []

    #number of mutations that are satisfied by each clone tree - starts off at 0
    mutations_per_ct = []
    
    #list of all the clone trees
    all_clone_trees = mk_directed(get_clone_trees([0, 1, 2, 3]))
    for i in range(len(all_clone_trees)):
        clone_tree_list.append(str(all_clone_trees[i]))
        mutations_per_ct.append(0)

    #get the overlapping mutations
    df_vcf['mutation_index'] = df_vcf.apply(lambda x: f'{x[0]}.{x[1]}.{x[3]}.{x[4]}', axis=1)
    selected_mutations = set(df_vcf['mutation_index']).intersection(set(df_clone_trees['mut_index']))
    #df_selected_clone_trees is the dataframe of df_clone_trees where the mutation index overlaps
    df_selected_clone_trees = df_clone_trees[df_clone_trees['mut_index'].isin(selected_mutations)]

    #total number of mutations
    num_rows = df_selected_clone_trees['mut_index'].nunique()

    #count the number of mutations that are satisfied by each clone tree
    for ct in df_selected_clone_trees['valid_clone_tree']:
        index = clone_tree_list.index(str(ct))
        mutations_per_ct[index] += 1
    #fraction of mutations that satisfy each clone tree (for the y axis)
    #list of length 16
    fraction_per_ct = []
    for num_mut in mutations_per_ct:
        fraction_per_ct.append(num_mut/num_rows)
    data = {"Clone Tree Number": clone_tree_index,
                    "Fraction of Mutations w/ Clone Tree": fraction_per_ct}

    # Creating histogram
    #x-axis is clone_tree_index [0, 1, 2, 3, ...]
    #y-axis is the fraction [0.88, 0.75, ...]
    plt.bar(clone_tree_index, fraction_per_ct, tick_label = clone_tree_index, color = 'black')
    plt.xlabel("Clone Tree Number")
    plt.ylabel("Fraction of Mutations w/ Clone Tree")
    plt.title("Fraction of Mutations per Clone Tree")
    plt.ylim(0, 1.2)
    plt.axhline(y=1, color='red', linestyle='--', linewidth=2)
    plt.show()