from mk_directed import mk_directed
from parse_state_tree import parse_state_tree
from rm_duplicates import rm_duplicates
from map_clone_trees import map_clone_trees
from get_clone_trees import get_clone_trees
from get_cn_clones import get_cn_clones
from collapse import collapse
from get_prufer_edges import get_prufer_edges
from is_valid_tree import is_valid_tree
from map_single_clone_tree import map_single_clone_tree
from plot_fractions import plot_fractions
from plot_violation import plot_violation
import pandas as pd
import numpy as np
from itertools import product
from matplotlib import pyplot as plt

#k14_output is the entire tsv file
k14_output = pd.read_csv('/Users/kyletsai/Desktop/SUMMER_2023/decifer/RA17_22_output/MPAM06_output_K14.tsv', sep='\t')
#print(k14_output)
num_rows = len(k14_output.index)
#best_input is the tsv file of the input (with mutation bins and copy number clones)
best_input = pd.read_csv('/Users/kyletsai/Desktop/SUMMER_2023/decifer/RA17_22_input/best.seg.ucn.tsv', sep='\t')
#df_vcf is the existing mutation file as a dataframe
df_vcf = pd.read_csv('/Users/kyletsai/Desktop/SUMMER_2023/decifer/Proj_06287_Q__RA17_22___SOMATIC.MuTect2.vep.FILLOUT.flt.noFFPE.JAM_filtered.vcf', 
                     comment='#', sep='\t', header=None)  


def main(k14_output, best_input, df_vcf):   
  ##main function 
  #
  #
  #
  final_mutation_index = []
  final_all_clone_trees = []
  #get all possible clone trees and make it directed with root 0
  all_clone_trees = mk_directed(get_clone_trees([0, 1, 2, 3]))

  for i in range(num_rows):
    #print("mutation" + str(i))
    #mutation_index is index of the mutation (10.52573509.G.GA)
    mutation_index = k14_output['mut_index'][i]

    #print(mutation_index)

    #chr_number is chromosome number of the mutation (10)
    chr_number = int(mutation_index.split('.')[0])
    ##print(chr_number)

    #chr_position is where the mutation is on the chromosome (52573509)
    chr_position = int(mutation_index.split('.')[1])
    #print(chr_position)


    #parse the state_tree data --> get the state tree for the given mutation
    state_tree = parse_state_tree(k14_output['state_tree'][i])
    #print(state_tree)


    #chr_x is the tsv file where chromosome number = x
    chr_x = best_input[best_input['#CHR'] == chr_number]
    #row_number will be the row index of the mutation bin for 52573509 (837)
    row_number = chr_x[(chr_x['START'] < chr_position) & (chr_x['END'] > chr_position)].index[0]
    #print(row_number)

    #cn_clones is a dictionary with key: value pairs as the clone number: the allele specific copy numbers
    cn_clones = get_cn_clones(best_input, row_number)
    #print(cn_clones)

    #all the clone trees mapped onto a state tree
    all_mapped_clone_trees = map_clone_trees(all_clone_trees, cn_clones)

    for index in range(len(all_mapped_clone_trees)):
      mapped_clone_tree = collapse(all_mapped_clone_trees[index])
      rm_duplicates(mapped_clone_tree)
      if is_valid_tree(mapped_clone_tree, state_tree):
        final_all_clone_trees.append(all_clone_trees[index])
        final_mutation_index.append(mutation_index)
  data = {'mut_index': final_mutation_index,'valid_clone_tree': final_all_clone_trees}
  df_clone_trees = pd.DataFrame(data)

  #PLOTTING THE RESULTS
  #index of each clone tree (just a list from 1-16)
  clone_tree_index = []
  for i in range(len(all_clone_trees)):
    clone_tree_index.append(i+1)
  
  plot_fractions(df_clone_trees, df_vcf, clone_tree_index)
  plot_violation(best_input, clone_tree_index)

#sar
main(k14_output, best_input, df_vcf)