#### script for filtering and renaming reads
from __future__ import print_function
import os
from commands import getoutput

allfiles=getoutput('ls SRR*/accep*').split()

for i in allfiles:
	out=i.split('/')[0]+'_good.bam'
	print('Start cleaning')
	os.system('samtools view -bq 10 %s > %s' % (i, out))
	print(i, getoutput('samtools view -c %s' % out), sep='\t', file=open('cleaned_stats.txt', 'a'))
	print('Remove older aligned file')
	os.system('rm %s' % i)


