######script for creating coexpression networks
###### create bunch of file in which there is the file name that is the geneofinterest (GOI) and for each line line[0] is geneid and line[1] is the PCC
from __future__ import print_function, division
import numpy
from scipy import stats
import sys
########################################
def calculate_r(gene, allgene, d):
	comp=allgene[:]
	comp.remove(gene)##### remove gene
	for i in comp:### start looping
		r=stats.pearsonr(d[gene], d[i])
		if numpy.isnan(r[0]) is not True: ##### identify sites with correlation coefficient
			print(i, r[0], sep='\t', file=open(gene, 'a'))

##########################################################

exp_table=sys.argv[1]  # count_table data
exp_d={}

for line in open(exp_table):
	if 'Phvul' in line:
		line=line.strip().split('\t')
		name=line[0]
		exp=[float(i) for i in line[1:]]
		##### try without removing genes with count < 1
		val=[i for i in exp if i >=10] ### identify values >=10
		if len(val)/len(exp)>=0.6: #### keep only sites where expression higher than 10 in 60% of the genotypes
			exp_d[name]=exp


genelist=list(exp_d.keys())
for i in genelist:
	calculate_r(i, genelist, exp_d)
