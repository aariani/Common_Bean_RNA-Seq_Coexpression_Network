# Common Bean RNA-Seq Coexpression Network

This repo contains correlation coefficients based on expression analysis of 85 RNA-Seq datasets. The RNA-Seq data were downloaded from the [NCBI SRA archive] (http://www.ncbi.nlm.nih.gov/sra).

In the folder "Pipelines" there are the scripts used for creating this dataset (Refer to the readme file).

In the folder "Coexpression_Data" there are 2 files with the inferred Coexpression Network (using a correlation threshold >= 0.8) :

* Pvul_coexp_net.txt is a tab-delimited files with two column indicating a vertex between two edges (genes)
* Pvul_coexp_net_PCC.txt is a similar to Pvul_coexp_net.txt

These data could be used for inferring and extracting a coexpression network for this species.

The folder "raw_coexpression" contains 18053 files named with common bean gene ID accordingly to [Phytozome platform] (www.phytozome.net). 

Each file is tab delimited and contains 2 columns:

1. GeneID
2. Pearson Correlation Coefficient (PCC) between the gene that named the file and the gene in column 1.

