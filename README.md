# Common Bean RNA-Seq Coexpression Network

This repo contains correlation coefficient based on 85 RNA-Seq datasets downloaded from the [NCBI SRA archive] (http://www.ncbi.nlm.nih.gov/sra).

In the folder 'Pipelines' there are the scripts used for creating this dataset (Refer to the readme file).

These data could be used for inferring and extracting a coexpression network for this species.

The folder "raw_coexpression" contains 18053 files named with common bean gene ID accordingly to [Phytozome platform] (www.phytozome.net). 

Each file is tab delimited and contains 2 columns:

1. GeneID
2. Pearson Correlation Coefficient (PCC) between the gene that named the file and the gene in column 1.

