# GeDiLiP: Gene-Disease Link Prediction Model Using Protein Sequence and Disease Definement

GeDiLiP (Gene-Disease Link Prediction Model) is a machine learning model that is used to predict gene-disease association.Model use protein seqeunce and disease definement. Protein sequence is vectorized by [ProtT5 Model](https://www.uniprot.org/help/downloads#embeddings:~:text=protein%20per%2Dresidue-,Homo%20sapiens,-per%2Dprotein%20per) that generated vectors saved in a file (per-protein.h5). Disase definement is vectorized by [BioBert v1.1 Model](https://huggingface.co/dmis-lab/biobert-v1.1) vectorization operation that was created by [DMIS-Lab](https://dmis.korea.ac.kr). In this project, dataset was gathered from [Disgenet (v7.0)](https://www.disgenet.org/dbinfo#:~:text=Version%20History-,May%204%2C%202020,-DisGeNET%20Database%207.0). In Disgenet(v7.0), contains 1,134,942 gene-disease associations (GDAs), between 21,671 genes and 30,170 diseases, disorders, traits, and clinical or abnormal human phenotypes.
In addition, gene-gene associations and disease-disease associations are added. Gene-gene associations were downloaded from [BioGrid v4.4.217](https://downloads.thebiogrid.org/File/BioGRID/Release-Archive/BIOGRID-4.4.217/BIOGRID-ORGANISM-4.4.217.tab.zip). In this project, only homo-sapiens' genes were used. Disease-disesae associations were gathered from DisGeNet via [API](https://www.disgenet.org/api/#/DDA:~:text=org/dbinfo%23section45-,Disease%2DDisease%20Associations%20(DDAs),-The%20DDAs%20service). In this model, train/validation/test split is splited based on [Uniref50](https://www.uniprot.org/help/uniref#:~:text=e.g.%C2%A0%22UniRef90_P99999%22.-,UniRef50,-UniRef50%20is%20generated)




&nbsp;

## Development and Dependencies

### This project can be run every operating system. However, ***Ubuntu 22.04.3*** is recommanded.
- Python 3
- Pip3
- Clone repository
- Install dependencies

    - all test run on CPU, if you want to run other devices, you should change some packages.
    - in Ubuntu (Recommended) or MacOS, 
    ```
        pip3 install -r requirementsUbuntu.txt
    ```
    - in Windows,
    ```
        pip3 install -r requirements.txt
    ```
    
    

&nbsp;

## Descriptions of folders and files in the GeDiLiP repository 


&nbsp;

## GeDiLiP Usage

This section intends to guide the users on how to run GeDiLiP. 

:warning: :warning: 

First of all, please readme files inside **source-files** and **graph-files** folders. File unzip operations are required. File unzip operations' command is written in readme files in **source-files** and **graph-files** folders.

:warning: :warning:

1. GeDiLiP on customized dataset is stored in **Main-Project** folder. 
2. GeDiLiP on SkipGNN's dataset(DisGeNet-curated) is stored in **Comparison-SkipGNN** folder. 
3. GeDiLiP on OGB's dataset(ogbl-biokg) is stored in **Comparison-SkipGNN** folder. 

There is a readme file inside of the every project folder.
There is a project diagrams [file](master-project-diagrams.drawio) that is built in drawio.  
&nbsp;

## License
Copyright (C) 2023 HUBioDataLab

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.