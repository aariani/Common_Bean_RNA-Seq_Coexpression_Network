## This folder cointains the scripts and files used for creating the Coexpression network dataset

=================================================================================================


### Name of the files and relative content

*	`Pvulgaris_genes_normalized_FPKM.txt`: Tab-delimited file with the normalized FPKM obtained by running `cuffnofm` with default parameters. Rows represent gene ID, columns represent the processed files downloaded from [NCBI SRA Archive] (http://www.ncbi.nlm.nih.gov/sra). The SRA run IDs for the columns are available on the `samples.table' files

*	`samples.table': Tab-delimited file containing the column names in `Pvulgaris_genes_normalized_FPKM.txt` and the relative SRA run ID of the processed file

*	`calc_PCC.py`: Python script for calculating Pearson Coerraltion Coefficient (PCC) between the genes in `Pvulgaris_genes_normalized_FPKM.txt` (See below)

*	`download_and_align.py`: Python script for downloading and aligning the different RNA-Seq datasets, accordingly to the informations in the `datalog.csv` file

*	`datalog.csv`: Comma-delimited file with the SRA Run ID, download path (as 17 Oct 2015), and Sequencing protocol (Paired/single end) 

*	`filter_alignments.py`: Python script for filtering alignments

=================================================================================================

## How to calculate the raw PCC data

The raw PCC data could be calculated using the `Pvulgaris_genes_normalized_FPKM.txt` files and the `calc_PCC.py` script.
For running the `calc_PCC.py` script you will need to install also the [numpy] (http://www.numpy.org/) and [scipy] (https://www.scipy.org/) libraries of python.

By default `calc_PCC.py` parses the `Pvulgaris_genes_normalized_FPKM.txt` files for obtaining the PCC data across different gene pairs.
The program considers only genes with detectable expression (i.e. FPKM > 10) in 60% of the RNA-seq data present in the expression table.

The output files are saved in the `Raw_PCC` folder. Each file is tab-delimited and contains 2 columns:

1. GeneID
2. PCC between the gene that named the file and the gene in column 1.

These data are could be used for extracting common bean coexpression network using custom PCC threshold.
The network could be inferred using the `inferNetwork` script in the parent folder.

If you want to modify the default parameters of the `calc_PCC.py` program type:

	python calc_PCC.py -h
	usage: python calc_PCC.py [-h] [-i EXP_MAT] [-m MINPRESENCE] [-o OUTFOLDER]
	Program for calculating PCC between genes based on the
	Pvulgaris_genes_normalized_FPKM.txt file
	optional arguments:
	   -h, --help               show this help message and exit
	   -i EXP_MAT, --input EXP_MAT
                        	    The Normalized expression matrix for common bean genes
                       		    (Default: Pvulgaris_genes_normalized_FPKM.txt)
	   -m MINPRESENCE, --min MINPRESENCE
                        	    The minimum percentage (in decimal) of dataset where a
                        	    gene is expressed (Default: 0.6 i.e. 60/100)
  	   -o OUTFOLDER, --output OUTFOLDER
                        	    The output folder of the PCC data
	

