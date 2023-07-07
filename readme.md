## Prerequisites 

## Usage Instructions

```
usage: python dcf_analysis.py [-h] --dcfout DCFOUT --dcfin DCFIN --op1 OP1 --op2 OP@ --plt1 PLT1 --plt2 PLT2 

-h          show this help message and exit 
--dcfout    csv file with decifer output
--dcfin     csv file with decifer input
--xref      csv file with mutations to subset with decifer files
--op1       output prefix 1 - valid clone trees per mutation locus
--op2       output prefix 2 - invalid clone trees, the invalid edge, and the corresponding  violating bin
--plt1      output prefix for plot 1 - fraction of valid mutations per clone tree
--plt2      output prefix for plot 2 - number of violations per clone tree
```
An example of using this function is 

```
python dcf_analysis.py --dcfout data/MPAM06_output_K14.tsv --dcfin data/best.seg.ucn.tsv --xref data/Proj_06287_Q__RA17_22___SOMATIC.MuTect2.vep.FILLOUT.flt.noFFPE.JAM_filtered.vcf --op1 test --op2 test --plt1 test --plt2 test

```

### Input/Output
There are 3 required input files. 

One input (dcfin) is a tsv file detailing mutation bins and copy number states for each clone. 

| #CHR  |START     | END     | SAMPLE  | cn_normal  | cn_clone1 | cn_clone2 | cn_clone3 |
| ---   | ---------| --------|---------| ---------- |-----------|-----------|-----------|
| 1     |1         |26314488 |MPAM06PT1|    1\|1	| 2\|2	    |	2\|2 	| 2\|2	    |
| 1     |26314488  |26644978 |MPAM06PT1|    1\|1	| 2\|2	    |	2\|2 	| 2\|1	    |
| 1     |26644978  |40002884 |MPAM06PT1|    1\|1	| 2\|2	    |	2\|2 	| 2\|2	    |


The second input (dcfout) is a tsv file containing the mutation locus and the inferred state tree from decifer (must be in following format)

| mut_index        | state_tree                                                          |
| -----------------| --------------------------------------------------------------------|
|10.52573509.G.GA  | (1,1,0)->(1,1,1);(1,1,0)->(2,1,0);(1,1,1)->(2,2,2);(2,2,2)->(3,2,2) |
|10.52589948.C.G   | (1,1,0)->(2,1,0);(1,1,0)->(2,2,0);(2,1,0)->(3,2,0);(3,2,0)->(3,2,1) |

The third input (xref) is a vcf file of high confidence mutations for cross referencing with the mutations in dcfout

| #CHROM      | POS              | REF              |ALT           |
| ------------| -----------------| -----------------| -------------|
| 16          |34982228          |A                 | C            |
| 10          |52573509          |G                 | GA           |



## Example