# Common Bean RNA-Seq Coexpression Network

###This repo contains Coexpression Network and Pearson Correlation Coefficients (PCC) based on expression analysis of 85 RNA-Seq datasets. 
The RNA-Seq raw data were downloaded as sequencing reads from the [NCBI SRA archive] (http://www.ncbi.nlm.nih.gov/sra).

===========================================================================================================

In the folder `Pipelines` there are the scripts used for creating this dataset.
If you want to re-create or create a modified version of this dataset refer to the README file inside the `Pipelines` folder.

In the folder `Coexpression_Data` there are 2 files with the inferred Coexpression Network:

* `Pvul_coexp_net.txt` is a tab-delimited file with two columns indicating an edge between two nodes (genes)
* `Pvul_coexp_net_PCC.txt` is a similar to `Pvul_coexp_net.txt` but contains a 3rd column showing the PCC.

Both the files used a PCC threshold of 0.8
These data are compatible with several programs for network visualization and analysis like [Cytoscape] (http://cytoscape.org/) and could be directly used for research studies

===========================================================================================================

## Download this repo

For clone this folder to your computer first you need to install git.
Let us assume you want to clone this repo into a directory named `proj`, you will need to open the terminal and type:

    mkdir proj
    cd proj
    git clone https://github.com/aariani/Common_Bean_RNA-Seq_Coexpression_Network

   
===========================================================================================================

## Extract coexpression network

For extracting the coexpression network you will need first to create the raw PCC data following the instructions in the `Pipelines` folder.
After re-creating the raw PCC you will need the `inferNetwork` script for create the coexpression network. 
This is a simple Python script, so just make sure you have python installed on your computer (Python 2.7+).
 
First you need to make the script executable, so from the command-line type:

    cd Common_Bean_RNA-Seq_Coexpression_Network
    chmod +x inferNetwork

Execute the script in the same folder where the `raw_coexpression` folder is. This folder contains the raw PCC data.

To see the command-line option type from the terminal:

    inferNetwork -h
        usage: inferNetwork [-h] [-i INPUTFOLDER] [--pcc] [-t MINPCC] [-o OUTPUTFILE]
        Program for exctracting coexpression network based on Pearson Correlation
        Coefficient (PCC) data
        optional arguments:
		-h, --help          show this help message and exit
        	-i INPUTFOLDER, --input INPUTFOLDER
                                The folder containing the Raw Coexpression data
                                (Default: raw_coexpression)
        	--pcc           Do you want to export also the PCC value between genes?? (Default: False)
        	-t MINPCC, --threshold MINPCC 
				Threshold of the PCC values for identifying an edge between two nodes.
                       		If positive the gene pairs with PCC < than this will be
                        	discarded. If negative the gene pairs with PCC > than this
                        	will be discarded (Default: 0.8)    
		-o OUTPUTFILE, --output OUTPUTFILE      
                                Name of output file (Default: CoexpressionNetwork.txt)

This script allows also to infer network with negative PCC that could be indicative of negative interaction (repression) between two genes (`-t` parameter).
