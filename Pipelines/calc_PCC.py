######script for creating coexpression networks
###### create bunch of file in which there is the file name that is the geneofinterest (GOI) and for each line line[0] is geneid and line[1] is the PCC
from __future__ import print_function, division
import numpy
from scipy import stats
import sys, os, argparse

parser=argparse.ArgumentParser(prog='calc_PCC.py', description='Program for calculating PCC between genes based on the Pvulgaris_genes_normalized_FPKM.txt file')
parser.add_argument('-i', '--input', dest='exp_mat', default='Pvulgaris_genes_normalized_FPKM.txt', help='The Normalized expression matrix for common bean genes (Default: Pvulgaris_genes_normalized_FPKM.txt)')
parser.add_argument('-m', '--min', dest='minpresence', default=0.6, type=float, help=r"The minimum percentage (in decimal) of dataset where a gene is expressed (Default: 0.6 i.e. 60/100)")
parser.add_argument('-o', '--output', dest='outfolder', default='Raw_PCC', help='The output folder of the PCC data')

args=parser.parse_args()

ifile=args.exp_mat
minpresence=args.minpresence
ofolder=args.outfolder


########################################
def calculate_r(gene, allgene, d):
	comp=allgene[:]
	comp.remove(gene)##### remove gene
	for i in comp:### start looping
		r=stats.pearsonr(d[gene], d[i])
		if numpy.isnan(r[0]) is not True: ##### identify sites with correlation coefficient
			print(i, r[0], sep='\t', file=open(gene, 'a'))

##########################################################

exp_d={}
for line in open(ifile):
	if 'Phvul' in line:
		line=line.strip().split('\t')
		name=line[0]
		exp=[float(i) for i in line[1:]]
		##### try without removing genes with count < 1
		val=[i for i in exp if i >=10] ### identify values >=10
		if len(val)/len(exp)>=minpresence: #### keep only sites where expression higher than 10 in 60% of the genotypes
			exp_d[name]=exp


genelist=list(exp_d.keys())
for i in genelist:
	calculate_r(i, genelist, exp_d)


os.system('mkdir %s' % ofolder)
os.system('mv Phvul* %s' % ofolder)
