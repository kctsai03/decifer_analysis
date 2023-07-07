
from parse_inputs import parse_state_tree, get_cn_clones
from get_clone_trees import mk_directed, get_clone_trees
from check_tree import map_clone_trees, is_valid_tree
from parse_inputs import get_cn_clones
from collapse import collapse, rm_duplicates
from plot import plot_fractions, plot_violation
import pandas as pd
import argparse
import numpy as np
from matplotlib import pyplot as plt

# #k14_output is the entire tsv file
# k14_output = pd.read_csv('/Users/kyletsai/Desktop/SUMMER_2023/decifer/RA17_22_output/MPAM06_output_K14.tsv', sep='\t')
# #print(k14_output)
# num_rows = len(k14_output.index)
# #best_input is the tsv file of the input (with mutation bins and copy number clones)
# best_input = pd.read_csv('/Users/kyletsai/Desktop/SUMMER_2023/decifer/RA17_22_input/best.seg.ucn.tsv', sep='\t')
# #df_vcf is the existing mutation file as a dataframe
# df_vcf = pd.read_csv('/Users/kyletsai/Desktop/SUMMER_2023/decifer/Proj_06287_Q__RA17_22___SOMATIC.MuTect2.vep.FILLOUT.flt.noFFPE.JAM_filtered.vcf', 
#                      comment='#', sep='\t', header=None)  


def main(args):   
  ##main function 
  #
  #
  #
  #getting the files from args
  if args.dcfout:
    dcfout = pd.read_csv(args.dcfout, sep='\t')
  if args.dcfin:
    dcfin = pd.read_csv(args.dcfin, sep='\t')
  if args.xref:
    df_vcf = pd.read_csv(args.xref, comment='#', sep='\t', header=None)
  if args.op1:
    op1 = f'{args.op1}_valid_clone_trees.tsv'
  if args.op2:
    op2 = f'{args.op2}_clone_tree_violations.tsv'
  if args.plt1:
    plt1 = f'{args.plt1}_fraction_of_valid_mut.pdf'
  if args.plt2:
    plt2 = f'{args.plt2}_num_violations_per_clone_tree.pdf'


  num_rows = len(dcfout.index)

  final_mutation_index = []
  final_all_clone_trees = []

  #get all possible clone trees and make it directed with root 0
  num_clones = 1
  for col in dcfin.columns:
    if 'cn_clone' in col:
      num_clones += 1
  ls_vertices = list(range(num_clones))
  all_clone_trees = mk_directed(get_clone_trees(ls_vertices))

  for i in range(num_rows):
    #print("mutation" + str(i))
    #mutation_index is index of the mutation (10.52573509.G.GA)
    mutation_index = dcfout['mut_index'][i]

    #print(mutation_index)

    #chr_number is chromosome number of the mutation (10)
    chr_number = int(mutation_index.split('.')[0])
    ##print(chr_number)

    #chr_position is where the mutation is on the chromosome (52573509)
    chr_position = int(mutation_index.split('.')[1])
    #print(chr_position)


    #parse the state_tree data --> get the state tree for the given mutation
    state_tree = parse_state_tree(dcfout['state_tree'][i])
    #print(state_tree)


    #chr_x is the tsv file where chromosome number = x
    chr_x = dcfin[dcfin['#CHR'] == chr_number]
    #row_number will be the row index of the mutation bin for 52573509 (837)
    row_number = chr_x[(chr_x['START'] < chr_position) & (chr_x['END'] > chr_position)].index[0]
    #print(row_number)

    #cn_clones is a dictionary with key: value pairs as the clone number: the allele specific copy numbers
    cn_clones = get_cn_clones(dcfin, row_number)
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
  df_clone_trees.to_csv(op1, sep="\t")


  #PLOTTING THE RESULTS
  #index of each clone tree (just a list from 1-16)
  clone_tree_index = []
  for i in range(len(all_clone_trees)):
    clone_tree_index.append(i+1)
  
  plot_fractions(df_clone_trees, df_vcf, clone_tree_index, all_clone_trees, plt1)
  output2 = plot_violation(dcfin, clone_tree_index, all_clone_trees, plt2)
  output2.to_csv(op2, sep="\t")


if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument('--dcfout', type=str, help='csv file with decifer output', required=True)
  parser.add_argument('--dcfin', type=str, help='csv file with decifer input', required=True)
  parser.add_argument('--xref', type=str, help='csv file with mutations to subset with decifer files')
  parser.add_argument('--op1', type=str, help='output prefix 1 - valid clone trees per mutation locus', required = True)
  parser.add_argument('--op2', type=str, help='output prefix 2 - invalid clone trees, the invalid edge, and the corresponding violating bin', required = True)
  parser.add_argument('--plt1', type=str, help='output prefix for plot 1 - fraction of valid mutations per clone tree', required = True)
  parser.add_argument('--plt2', type=str, help='output prefix for plot 2 - number of violations per clone tree', required = True)
  args = parser.parse_args()
  main(args)


# #test commit 2
# main(k14_output, best_input, df_vcf)