# Common Bean RNA-Seq Coexpression Network

This repo contains Coexpression Network and Pearson Correlation Coefficients (PCC) based on expression analysis of 85 RNA-Seq datasets. The RNA-Seq data were downloaded from the [NCBI SRA archive] (http://www.ncbi.nlm.nih.gov/sra).

===========================================================================================================

In the folder "Pipelines" there are the scripts used for creating this dataset (Refer to the readme file inside the folder).

In the folder "Coexpression_Data" there are 2 files with the inferred Coexpression Network:
* Pvul_coexp_net.txt is a tab-delimited files with two column indicating a vertex between two edges (genes)
* Pvul_coexp_net_PCC.txt is a similar to Pvul_coexp_net.txt but contains a 3rd column showing the PCC.

Both the files used a PCC threshold of 0.8
These data could be directly used for research studies

===========================================================================================================
The folder "raw_coexpression" contains 18053 files named with common bean gene ID accordingly to [Phytozome platform] (www.phytozome.net). 

Each file is tab delimited and contains 2 columns:

1. GeneID
2. Pearson Correlation Coefficient (PCC) between the gene that named the file and the gene in column 1.

These data are intended for extracting Common bean coexpression network using custom PCC threshold
The network could be inferred using the inferNet script in this folder.

