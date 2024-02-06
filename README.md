# GeDiLiP: Gene-Disease Association Prediction Model Using Protein Sequence and Disease Definement

GeDiLiP (Gene-Disease Link Prediction Model) is a machine learning model that is used to predict gene-disease association.Model use protein seqeunce and disease definement. Protein sequence is vectorized by [ProtT5 Model](https://www.uniprot.org/help/downloads#embeddings:~:text=protein%20per%2Dresidue-,Homo%20sapiens,-per%2Dprotein%20per) that generated vectors saved in a file (per-protein.h5). Disase definement is vectorized by [BioBert v1.1 Model](https://huggingface.co/dmis-lab/biobert-v1.1) vectorization operation that was created by [DMIS-Lab](https://dmis.korea.ac.kr). In this project, dataset was gathered from [Disgenet (v7.0)](https://www.disgenet.org/dbinfo#:~:text=Version%20History-,May%204%2C%202020,-DisGeNET%20Database%207.0). In Disgenet(v7.0), contains 1,134,942 gene-disease associations (GDAs), between 21,671 genes and 30,170 diseases, disorders, traits, and clinical or abnormal human phenotypes.
In addition, gene-gene associations and disease-disease associations are added. Gene-gene associations were downloaded from [BioGrid v4.4.217](https://downloads.thebiogrid.org/File/BioGRID/Release-Archive/BIOGRID-4.4.217/BIOGRID-ORGANISM-4.4.217.tab.zip). In this project, only homo-sapiens' genes were used. Disease-disesae associations were gathered from DisGeNet via [API](https://www.disgenet.org/api/#/DDA:~:text=org/dbinfo%23section45-,Disease%2DDisease%20Associations%20(DDAs),-The%20DDAs%20service). 




&nbsp;

## Development and Dependencies

- Python 3
- Pip3
- Clone repository
- Install dependencies
    - all test run on CPU, if you want to run other devices, you should change some packages.
    - in windows,
    ```
        pip3 install -r requirements.txt
    ```
    - in ubuntu,
    ```
        pip3 install -r requirementsUbuntu.txt
    ```
    

&nbsp;

## Descriptions of folders and files in the GeDiLiP repository 


&nbsp;

## GeDiLiP Usage

This section intends to guide the users on how to install and run ASCARIS to produce numerical SAV representations. 

Please (i) clone this repository to your local server, and (ii) download all the requirements by running the following code:
```
pip3 install -r requirements.txt

```
Please unzip required files as described in the **Input Files** section prior to running the code. All is set at this point. ASCARIS can be run in three different settings:

1. Running ASCARIS for only one SAV datapoint:

```
python3 code/main.py -s 1 -i Q00889-H-85-D -impute True
```
2. Running ASCARIS for more than one datapoints:
```
python3 code/main.py -s 2 -i 'P41180-E-604-K, Q16363-Y-498-H' impute False
```

3. Running ASCARIS using a tab-separated file containing the SAV data points. Please see sample_input.txt for the format.
```
python3 code/main.py -s 2 -i input_files/sample_input.txt
```

### Input Arguments

-s :  selection for input structure data. (1: Use PDB-ModBase-SwissModel structures, 2: Use AlphaFold Structures) </br>

-i :  input option. Enter datapoint to predict or input file path in the following form:</br>
- *Option 1: Comma-separated list of idenfiers (UniProt ID-wt residue-position-mutated residue (e.g. Q9Y4W6-N-432-T or Q9Y4W6-N-432-T, Q9Y4W6-N-432-T))*  
- *Option 2: Enter tab-separated file path*

-impute :  Boolean for the imputation of NaN values in the dataset. Imputation is done by taking the median value of corresponding column/feature. Default: True </br>

### Input Files 

Files that are necessary to run the ASCARIS tool are found under the **input_files** folder.

- **swissmodel_structures.txt.zip** : Includes summary file for Swiss-Model structures. Swiss-Model summary (INDEX-metadata) files are downloaded separately for each organism from https://swissmodel.expasy.org/repository, and merged into a single file by running create_swissmodelSummary.py code file. Resulting file is uploaded to GitHub as a zip file due to size limitations, thus **please unzip this file to input_files folder prior to running ASCARIS**.
-   Alternatively it can be downloaded [here](https://drive.google.com/drive/u/1/folders/1pJyXcguupyGggl25fzbRWwwqC6qUbDka). If needed, the user can create an updated file by running script **create_swissmodelSummary.py** in the directory in which newly downloaded Swiss-Model meta-data is found (folder_to_meta_data). Example command line is given below. Resulting output file will be created under /input_files.
```
cd ASCARIS
python3 code/create_swissmodelSummary.py -folder_name folder_to_meta_data
```

- **domains.txt** : Includes InterPro domains simplified as in the following order *(tab separated)* --> 
  [uniprotID      domainID        domainStartPosition     domainEndPosition]
  
- **significant_domains** :  Selected domains from *domains.txt* file according to the results of the Fisher's exact test, which was applied to all domains in the training test to assess their significance with respect to the variant effect outcome (neutral or deleterious). p_value is chosen as 0.01.

- **H_sapiens_interfacesHQ.txt** :  High confidence interfaces downloaded from [Interactome Insider](http://interactomeinsider.yulab.org/downloads.html) for *Homo sapiens*

- **alphafold_structures** : This folder is designated to contain Alphafold structure files. **Please download the '.tar' file from [AlphaFold Human proteome predictions](http://ftp.ebi.ac.uk/pub/databases/alphafold/latest/) to the input_files folder and untar here**. Summary file (alphafold_summary) is provided in the input files folder for v4 build. If you are using a build different than the currently present in ASCARIS repo (v4), **run get_alphafoldStructures.py** to untar the structures and create a new alphafold_summary file. The current alphafold_structures folder in this repository contains only 100 AlphaFold model files for demo purposes (due to file size limitation), hence the users need to untar the complete set of AlphaFold structures here prior to running ASCARIS. Example command line for build v4 is given below.
  
```
cd ASCARIS
python3 code/get_alphafoldStructures.py -file_name UP000005640_9606_HUMAN_v4.tar
```

- **alphafold_summary**: Processed data for AlphaFold structures. Includes protein identifier, chain id, sequence, model count for each entry.

### Output Files 

Results (output) of ASCARIS runs can be found in the **out_files** folder.

&nbsp;


### Sample Run 

Example The input file format is shown below (using the **sample_input.txt**). Columns represent the UniProt ID of the protein, wild type amino acid, position of the amino acid change, and the mutated amino acid, respectively. Input file must be given **without** a header.


```
Q16363	Y	498	H
P23560	V	66	M
Q00889	H	85	D
P04217	H	52	R
P16219	R	46	W
```

Upon running ASCARIS, the output files will be saved in **out_files** folder. Depending on the selected arguments, two type of sub-folders (PDB and AlphaFold) will be created. 

*__If the user wants to run ASCARIS using PDB-ModBase-SwissModel structures, the argument -s should be set to 1:__*

```
python3 code/main.py -s 1 -i input_files/sample_input.txt
```

Upon running the line above, the folllowing files will be generated: 

- **pdb/pdb_structures** : Contains downloaded structure files from PDB for input proteins when applicable. If the user has a folder wherein PDB structures are stored, please change the name of that folder to pdb_structures and the extension of files to '.txt' to decrease run time. 
- **pdb/swissmodel_structures** : Contains downloaded model files from SwissModel for input proteins when applicable.
- **pdb/modbase_structures** : Contains downloaded model files from ModBase for input proteins when applicable. Each file contains all models related to one protein.
- **pdb/modbase_structures_individual** : Contains downloaded model files from ModBase for input proteins when applicable. Each file contains individual models related to one protein.
- **pdb/alignment_files** : Contains alignment files of protein sequences. 
- **pdb/3D_alignment** : Contains alignment files of structure files. This step is performed in order to avoid missing residues in the PDB files.
- **pdb/sasa_files** : Contains calculated solvent accessible surface area values for each data point.
- **pdb/feature_vector.txt** : The final feature vector file.
- **pdb/log.txt** : Log file.


*__If the user wants to run ASCARIS using Alphafold models, the argument -s should be set to 2:__*

```
python3 code/main.py -s 2 -i input_files/sample_input.txt
```

Upon running the line above, the folllowing files will be generated: 

- **alphafold/alignment_files** : Contains alignment of UniProt sequence files.
- **alphafold/3D_alignment** :  Contains alignment of UniProt sequence files to PDB sequence files.
- **alphafold/sasa_files** : Contains calculated solvent accessible surface area values for each data point.
- **alphafold/featurevector_alphafold.txt** : Final feature vector file.
- **alphafold/log.txt** : Log file

&nbsp;

## Description of the Dimensions of ASCARIS SAV Representations

<img width="1503" alt="ASCARIS_Representation_Dimensions" src="https://github.com/HUBioDataLab/ASCARIS/assets/26777185/4d560f9f-d847-44c7-8959-cb7f14927012">

In ASCARIS representations, dimensions 1-5 correspond to datapoint identifier, 6-9 correspond to physicochemical property values, 10-12 correspond to domain-related information, 13-14 correspond to information regarding variation's position on the protein (both the sasa value and the categorization), 15-44 correspond to binary correspondence between the variation and different types of positional annotations (1 dimension for each annotation type, for a total of 30 types), 45-74 correspond to spatial (Euclidian) distances between the variation and different types of positional annotations (1 dimension for each annotation type, for a total of 30 types).


| Order of dimension | Column name in the output file  | Description |  Source | 
| ------------- | ------------- | ------------- | ------------- |
| 1 | prot_uniprotAcc | UniProt accession | Metadata obtained from UniProtKB/Swiss-Prot |
| 2 | wt_residue | Wild type residue | Data obtained from UniProtKB/Swiss-Prot (humsavar), ClinVar, PMD |
| 3 | mut_residue | Mutated residue | Data obtained from UniProtKB/Swiss-Prot (humsavar), ClinVar, PMD |
| 4 | position | Variation position | Data obtained from UniProtKB/Swiss-Prot (humsavar), ClinVar, PMD |
| 5 | meta_merged | Datapoint identifier (UniProt accession-WT Residue-VariationPosition-Mutated Residue) | - |
| 6 | composition | Change in composition values upon the occurrence of variation. Composition is defined as the atomic weight ratio of hetero (non-carbon) elements in end groups or rings to carbons in the side chain. | Literature |
| 7 | polarity | Change in polarity values upon variation. | Literature |
| 8 | volume | Change in volume values upon variation. | Literature |
| 9 | granthamScore | Change in Grantham scores (the combination of composition, polarity and volume) values upon variation. | Literature |
| 10 | domains_all | InterPro Domain IDs of all domains found in the dataset  | Data obtained from InterPro |
| 11 | domains_sig | InterPro Domain IDs of significant domains in the dataset. Domains that are not found to be significant in Fisher's Exact Test are labelled as "NULL". | Data obtained from InterPro |
| 12 | domains_3Ddist | Shortest Euclidian distance between the domain and the variation site. | A newly engineered feature (data obtained from PDB/AlphaFold and InterPro) |
| 13 | sasa | Solvent accessible surface area values. | FreeSASA |
| 14 | location_3state | Caterozied location of the variation in the structure: surface, core or interface. | FreeSASA, InteractomeInsider |
| 15-44 |disulfide_bin, intMet_bin,intramembrane_bin, naturalVariant_bin, dnaBinding_bin, activeSite_bin, nucleotideBinding_bin, lipidation_bin, site_bin, transmembrane_bin, crosslink_bin, mutagenesis_bin, strand_bin, helix_bin, turn_bin, metalBinding_bin, repeat_bin, caBinding_bin, topologicalDomain_bin, bindingSite_bin, region_bin, signalPeptide_bin, modifiedResidue_bin, zincFinger_bin, motif_bin, coiledCoil_bin, peptide_bin, transitPeptide_bin, glycosylation_bin, propeptide_bin | Positional sequence annotations, binary correspondence-based (30 different types of annotations, each one on a different dimension). Categories: 0: annotatation does not exist on the protein, 1: annotation is presented, but the variation is not on the annotated site, 2: variation is on the annotated site. | Newly engineered features (data obtained from UniProtKB) |
| 45-74 |disulfide_dist, intMet_dist, intramembrane_dist, naturalVariant_dist, dnaBinding_dist, activeSite_dist, nucleotideBinding_dist, lipidation_dist, site_dist, transmembrane_dist, crosslink_dist, mutagenesis_dist, strand_dist, helix_dist, turn_dist, metalBinding_dist, repeat_dist, caBinding_dist, topologicalDomain_dist, bindingSite_dist, region_dist, signalPeptide_dist, modifiedResidue_dist, zincFinger_dist, motif_dist, coiledCoil_dist, peptide_dist, transitPeptide_dist, glycosylation_dist, propeptide_dist | Positional sequence annotations, distance-based (the spatial distance between the annotated residue and the mutated residue, in the protein structure, for 30 different types of annotations, each one on a different dimension), in terms of Angstroms. | Newly engineered features (data obtained from PDB/AlphaFold and UniProtKB) |

&nbsp;

## Please Refer to Our Pre-print for More Information:

Cankara, F., & Dogan, T. (2022). ASCARIS: Positional Feature Annotation and Protein Structure-Based Representation of Single Amino Acid Variations. *bioRxiv*, 514934v1. [Link](https://www.biorxiv.org/content/10.1101/2022.11.03.514934v1)

&nbsp;

## License
Copyright (C) 2023 HUBioDataLab

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.