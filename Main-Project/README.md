# Main Project

This is the core project of GLADIGATOR, containing the proposed method for gene-disease association prediction. The project consists of three main components:

### 1. Build-Graph
This component builds customizable graph files from gathered sources including DisGeNET, BioGrid, and UniProt. The graphs are constructed based on gene-disease associations with customizable score thresholds.

**Key Features:**
- Creates graph files with different gene-disease score thresholds
- Incorporates multiple data sources for comprehensive graph construction
- Generates files in PyTorch format for model training

**Usage:**
```bash
# Build graph with gene-disease score >= 0.5
python3 build_graph.py 0.5

# Build graph with gene-disease score >= 0.1
python3 build_graph.py 0.1

# Build graph with gene-disease score >= 0.05
python3 build_graph.py 0.05
```

### 2. Gathering-Data
This component gathers data from various sources using APIs and processes it for graph construction.

**Data Sources:**
- **DisGeNET**: Gene-disease associations via API
- **UMLS**: Disease information via API
- **BioGrid**: Gene-gene associations
- **UniProt**: Protein sequence information

**Important**: Before running the data gathering programs, you must create a `config.py` file with API credentials:

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

### 3. Run-Model
This component trains and tests the deep learning model using the built graph files.

**Model Architecture:**
The model uses a graph neural network architecture with:
- Node embeddings for genes and diseases
- Edge features for associations
- Attention mechanisms for relationship learning

**Usage:**
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

### Project Structure
```
Main-Project/
├── Build-Graph/
│   ├── build_graph.py          # Graph construction script
│   ├── build-main-graph.png    # Graph construction visualization
│   └── README.md               # Build-Graph documentation
├── Gathering-Data/
│   ├── gather_disease_data_from_umls.py  # UMLS data gathering
│   ├── gather_gene_disease_information.py # DisGeNET data gathering
│   ├── README.md               # Data gathering documentation
│   └── config.py               # API configuration (create this file)
└── Run-Model/
    ├── run_model.py            # Model training and testing
    ├── main-algorithm.png      # Model architecture visualization
    ├── README.md               # Run-Model documentation
    └── results/                # Training results (auto-generated)
```

### Prerequisites
- Python 3.11
- PyTorch
- NetworkX
- Pandas
- NumPy
- Scikit-learn

### Installation
1. Create and activate a virtual environment
2. Install dependencies: `pip install -r requirements.txt`
3. Create `config.py` file in `Gathering-Data/` directory
4. Download and unzip source files from `source-files/` directory

### Usage Workflow
1. **Gather Data**: Run data gathering scripts to collect and process data
2. **Build Graph**: Create graph files with desired score thresholds
3. **Train Model**: Train and test the model using the graph files
4. **Evaluate Results**: Analyze the results in the generated CSV files

### Troubleshooting
- **Memory Issues**: Reduce batch size in `run_model.py` if encountering memory errors
- **API Errors**: Check API credentials in `config.py` and network connectivity
- **File Not Found**: Ensure all required files are downloaded and unzipped

