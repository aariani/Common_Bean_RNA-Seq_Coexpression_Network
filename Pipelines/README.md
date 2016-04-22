## This folder cointains the scripts and files used for creating the Coexpression network dataset

=================================================================================================


### Name of the files and relative content

*	`Pvulgaris_genes_normalized_FPKM.txt`: Tab-delimited file with the normalized FPKM obtained by running `cuffnofm` with default parameters. Rows represent gene ID, columns represent the processed files downloaded from [NCBI SRA Archive] (http://www.ncbi.nlm.nih.gov/sra). The SRA run IDs for the columns are available on the `samples.table' files

*	`samples.table': Tab-delimited file containing the column names in `Pvulgaris_genes_normalized_FPKM.txt` and the relative SRA run ID of the processed file

*	`calc_coexp.py`: Python script for calculatinf Pearson Coerraltion Coefficient (PCC) between the FPKM values in `Pvulgaris_genes_normalized_FPKM.txt`

*	`download_and_align.py`: Python script for downloading and aligning the different RNA-Seq datasets, accordingly to the informations in the `datalog.csv` file

*	`datalog.csv`: Comma-delimited file with the SRA Run ID, download path (as 17 Oct 2015), and Sequencing protocol (Paired/single end) 

*	`filter_alignments.py`: Python script for filtering alignments


