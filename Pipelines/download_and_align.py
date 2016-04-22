### pipeline for downloading and align dataset from different experiments
from __future__ import print_function
import sys, os, numpy
from commands import getoutput

def estimate_insert_size(fwd, rev):
	#### get insert size from sam alignment
	readl=100
	os.system('head -n 4000000 %s > prova_fwd.fastq' % fwd)
	os.system('head -n 4000000 %s > prova_rev.fastq' % rev)
	os.system('bwa mem ~/pvulgaris/annotation/bwa_cds/Pvulgaris_218_cds.fa prova_fwd.fastq prova_rev.fastq > prova_aln.sam')
	l=getoutput(r"grep -v '@SQ' prova_aln.sam |cut -f 6,9|grep -vF '*' |grep -v '-'|grep -v 0 |cut -f2").split('\n')
	l=[int(i) for i in l]
	ins_size=int(numpy.median(l)-readl)
	ins_stdev=int(numpy.std(l))
	return ins_size, ins_stdev

###############################################
def paired_protocol(a):
	####################### protocol for pe reads alignment 
	f=a+'.sra'
	os.system('fastq-dump --split-files ' + f) # extract reads
	print('Starting quality filtering reads')
	os.system('sickle pe -t sanger -f %s_1.fastq -r %s_2.fastq -o filt_fwd_%s.fastq -p filt_rev_%s.fastq -s non_paired -n' % (a, a, a, a))
	os.system('wc -l *fastq >> filt_info')
	os.system('rm %s.sra %s_1.fastq %s_2.fastq' % (a, a, a))
	fwdaln='filt_fwd_%s.fastq' % a
	revaln='filt_rev_%s.fastq' % a
	print('Start estimating inset size for PE reads')
	insize, stdev=estimate_insert_size(fwdaln, revaln)
	cmd='tophat2 -p4 -o %s -N 5 --read-gap-length 3 --read-edit-dist 5 -r %s --mate-std-dev %s -m 1 --no-novel-juncs -M --transcriptome-index=transcriptome_data/transcript ~/pvulgaris/assembly/tophat/Pvulgaris_218 %s %s' % (a, insize, stdev, fwdaln, revaln)
        print(cmd)
        os.system(cmd)
        os.system('rm %s %s' % (fwdaln, revaln))
##################################################

def single_protocol(b):
	f=b+'.sra'
	os.system('fastq-dump ' + f)
	os.system('sickle se -t sanger -f %s.fastq -o filt_%s.fastq -n' % (b, b))
	os.system('wc -l *fastq >> filt_info')
	os.system('rm %s.sra %s.fastq' % (b,b))
	alnfile='filt_%s.fastq' % b
	cmd='tophat2 -p4 -o %s -N 5 --read-gap-length 3 --read-edit-dist 5 -m 1 --no-novel-juncs -M --transcriptome-index=transcriptome_data/transcript ~/pvulgaris/assembly/tophat/Pvulgaris_218 %s' % (b, alnfile)
	print(cmd)
	os.system(cmd)
	os.system('rm %s' % alnfile)
#################################### Prepared all the protocols

datalog='datalog.csv' ### this is the modified datalog downloaded from SRA (runinfo file)
data_files=[]
for line in open(datalog):
	if 'SRR' in line:
		data_files.append(line)
####built a list with all the lines

while data_files:		
	line=data_files[0].strip().split(',')
	name=line[0]
	download_path=line[1]
	library=line[2]
	try:#### add try so avoid all the errors if there's no downloads
		os.system('wget '+ download_path) #### download file
		# start extracting and cleaning file
		if library=='PAIRED':
			paired_protocol(name)
		elif library=='SINGLE':
			single_protocol(name)
		data_files=data_files[1:]
	except:
		continue
	
