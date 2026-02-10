# GLADIGATOR: Graph Learning-based Disease Gene Association Prediction

GLADIGATOR is a machine learning model that predicts gene-disease associations using protein sequences and disease definitions. The model uses:

- **Protein sequences**: Vectorized using the [ProtT5 Model](https://www.uniprot.org/help/downloads#embeddings:~:text=protein%20per%2Dresidue-,Homo%20sapiens,-per%2Dprotein%20per), with vectors saved in `per-protein.h5`
- **Disease definitions**: Vectorized using the [BioBert v1.1 Model](https://huggingface.co/dmis-lab/biobert-v1.1) from [DMIS-Lab](https://dmis.korea.ac.kr)

The project uses data from [DisGeNET (v7.0)](https://www.disgenet.org/dbinfo#:~:text=Version%20History-,May%204%2C%202020,-DisGeNET%20Database%207.0), which contains 1,134,942 gene-disease associations (GDAs) between 21,671 genes and 30,170 diseases, disorders, traits, and clinical or abnormal human phenotypes.

Additional data includes:
- **Gene-gene associations**: Downloaded from [BioGrid v4.4.217](https://downloads.thebiogrid.org/File/BioGRID/Release-Archive/BIOGRID-4.4.217/BIOGRID-ORGANISM-4.4.217.tab.zip)
- **Disease-disease associations**: Gathered from DisGeNET via [API](https://www.disgenet.org/api/#/DDA:~:text=org/dbinfo%23section45-,Disease%2DDisease%20Associations%20(DDAs),-The%20DDAs%20service)

The model uses train/validation/test splits based on [UniRef50](https://www.uniprot.org/help/uniref#:~:text=e.g.%C2%A0%22UniRef90_P99999%22.-,UniRef50,-UniRef50%20is%20generated)




&nbsp;

## Development and Dependencies

### Supported Platforms
This project can run on any operating system, but **Ubuntu 22.04.3** is recommended.

### Prerequisites
- Python 3.11
- Pip3
- Virtual environment (venv)
- Git (for cloning the repository)

### Installation
1. Clone the repository:
2. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

**Note**: All tests run on CPU. To use other devices (GPU/TPU), you'll need to modify some packages in `requirements.txt`.

    
    

## Project Structure

The GLADIGATOR repository contains 4 main parts:

### 1. Main-Project
This is the core project containing the proposed method. It uses DisGeNET API data source with GDA score limitations and BioGrid data.

### 2. Comparison-SkipGNN
This project compares GLADIGATOR with other methods using the DisGeNET curated dataset. It also uses BioGrid data.

### 3. Comparison-Open-Graph-Dataset
This project compares GLADIGATOR with other methods using the OGB (ogbl-biokg) dataset. It also uses BioGrid data.

### 4. Make-Prediction
This contains trained models of the proposed methods. Users can make gene-disease association predictions by running `MakePrediction.py`.

Each project folder contains its own README file with detailed instructions.

## Usage

### Prerequisites
Before running the project, please:
1. Read the README files in the **source-files** and **graph-files** folders
2. Perform the required **UNZIP** operations (commands are provided in those README files)

### Project Steps
The proposed method consists of the following steps:

#### 1. Gathering-Data
This step gathers information from UMLS and DisGeNET using APIs.

**Important**: Before running the programs, you must create a `config.py` file with the required API credentials:

```python
config = {
    "email": "example@example.com",
    "password": "example",
    "apikey": "example-apikey"
}
```

**Note**: The DisGeNET API is currently unavailable. Please use the source files in the `source-files` folder instead.

**Commands**:
```bash
# To gather DisGeNET information
python3 gather_gene_disease_information.py

# To gather disease information from UMLS
python3 gather_disease_data_from_umls.py
```

#### 2. Build-Graph
This step builds customizable graph files from gathered sources (DisGeNET, BioGrid, UniProt).

**Input Parameter**: Gene-disease score threshold

**Example Usages**:
```bash
# Build graph with gene-disease score >= 0.5
python3 build_graph.py 0.5

# Build graph with gene-disease score >= 0.1
python3 build_graph.py 0.1

# Build graph with gene-disease score >= 0.05
python3 build_graph.py 0.05
```

#### 3. Run-Model
This step trains and tests the deep learning model using the built graph files.

**Input Parameter**: Path to the graph file

**Example Usages**:
```bash
# Run model with graph file for score >= 0.5
python3 run_model.py "../../graph-files/Graph_Own_0.5.pt"

# Run model with graph file for score >= 0.1
python3 run_model.py "../../graph-files/Graph_Own_0.1.pt"

# Run model with graph file for score >= 0.05
python3 run_model.py "../../graph-files/Graph_Own_0.05.pt"
```

**Output Files**: After training, the best validation and test results are stored in CSV files:
- `val-resultsGraph_Own_0.5.csv` and `test-resultsGraph_Own_0.5.csv`
- `val-resultsGraph_Own_0.1.csv` and `test-resultsGraph_Own_0.1.csv`
- `val-resultsGraph_Own_0.05.csv` and `test-resultsGraph_Own_0.05.csv`

#### 4. Make Prediction
Use trained models to make predictions between genes and diseases.

**Example**:
```bash
# Predict association between gene PRPH2 and disease C0016529
python3 MakePrediction.py Graph_Own_0.5_model.pth PRPH2 C0016529

# Predict association between gene AGER and disease C1518922
python3 MakePrediction.py Graph_Own_0.05_model.pth AGER C1518922
```

**Note**: The `config.py` file must be in the `./Make-Prediction` directory with the same format as above.



## **Gathering-Data**
------------------------
This part is used to gather information from UMLS and DisGeNet via using API. 


:warning:

Before run this programs, you must build config.py file that store required information when access UMLS and DisGeNet API.

Apikey is required to access [UMLS](https://uts-ws.nlm.nih.gov/rest/content/) server. Apikey is used to gather data from [UMLS](https://uts-ws.nlm.nih.gov/rest/content/) server, you can research in this [documentation](https://documentation.uts.nlm.nih.gov/rest/search/)

Email and password is used to enroll to the Disgenet, you can research in this [documentation](https://www.disgenet.org/api/). 

:warning:

DisGeNet API is not available at this moment. Please use source files in source-files folder. 


:warning:

Your config.py file must be inside of the ./Main-Project/Gathering-Data/ folder.

:warning:

Inside of the config.py file is mention in below

	config = {
		"email":"example@example.com",
		"password":"example",
		"apikey":"example-apikey"
	}


:warning:


if you want to gather DisGeNet informations, you should this command that mentioned in below.
```
	python3 gather_gene_disease_information.py
```

---


if you want to gather diseases informations from UMLS, you should this command that mentioned in below.

```
	python3 gather_disease_data_from_umls.py
```



:warning:

***python*** keyword is used to call ***python3*** in some machines. If your machine is like that, you can change ***python3*** keyword with ***python*** keyword.

## **Build-Graph**
------------------------

In this part, customizable graph files are built. Steps' of the build customizable graph is mentioned in below. 

:warning:

<p align="center"> 
    <img src="Main-Project/Build-Graph/build-main-graph.png">
</p>


### Input Parameter

Only input parameter is gene-disease score. 

#### Example Usages
For example, you want build a graph that gene-disease score is equal and more that 0.5, you can run this command.

```
    python3 build_graph.py 0.5
```

---

Another example, you want build a graph that gene-disease score is equal and more that 0.1, you can run this command.

```
    python3 build_graph.py 0.1
```

---

Another example, you want build a graph that gene-disease score is equal and more that 0.05, you can run this command.

```
    python3 build_graph.py 0.05
```


:warning:

***python*** keyword is used to call ***python3*** in some machines. If your machine is like that, you can change ***python3*** keyword with ***python*** keyword.


## **Run-Model**
------------------------

In this part, our deep learning model is trained and tested. Steps' of the train/test process and the model architecture are mentioned in below.

<p align="center"> 
    <img src="Main-Project/Run-Model/main-algorithm.png">
</p>



### Input Parameter
Only input parameter is a path of the graph file that is a dataset model is trained/tested on this dataset.

#### Example Usages
For example, you want run model with min gene-disase score is 0.5, you can call this command.
```
    python3 run_model.py "../../graph-files/Graph_Own_0.5.pt"
```

Another example, you want run model with min gene-disase score is 0.1, you can call this command.

```
    python3 run_model.py "../../graph-files/Graph_Own_0.1.pt"
```

Another example, you want run model with min gene-disase score is 0.1, you can call this command.

```
    python3 run_model.py "../../graph-files/Graph_Own_0.05.pt"
```


:warning:

***python*** keyword is used to call ***python3*** in some machines. If your machine is like that, you can change ***python3*** keyword with ***python*** keyword.

## Output Files

After train model operation is completed. Best validation and test result is stored in a csv file.

---

For example, you run this command, that is mentioned in below.
```
    python3 run_model.py "../../graph-files/Graph_Own_0.5.pt"
```

End of the train process, the best validation and test result are store in ***val-resultsGraph_Own_0.5.csv*** and ***test-resultsGraph_Own_0.5.csv***

---

Another example, you run this command, that is mentioned in below.

```
    python3 run_model.py "../../graph-files/Graph_Own_0.1.pt"
```

End of the train process, the best validation and test result are store in ***val-resultsGraph_Own_0.1.csv*** and ***test-resultsGraph_Own_0.1.csv***

---

Another example, you run this command, that is mentioned in below.

```
    python3 run_model.py "../../graph-files/Graph_Own_0.05.pt"
```

End of the train process, the best validation and test result are store in ***val-resultsGraph_Own_0.05.csv*** and ***test-resultsGraph_Own_0.05.csv***



## Make Prediction With Trained Models 

For example, you want to make prediction between gene PRPH2 and disease C0016529 via using Graph_Own_0.5_model.pth trained model. You should call this command
```
    python3 MakePrediction.py Graph_Own_0.5_model.pth PRPH2 C0016529
```

For example, you want to make prediction between gene AGER and disease C1518922 via using Graph_Own_0.05_model.pth trained model. You should call this command

```
    python3 MakePrediction.py Graph_Own_0.05_model.pth AGER C1518922
```

:warning:

Your config.py file must be inside of the ./trained-models.

:warning:

Inside of the config.py file is mention in below

	config = {
		"email":"example@example.com",
		"password":"example",
		"apikey":"example-apikey"
	}


:warning:



&nbsp;

## License

Copyright (C) 2023 HUBioDataLab

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
