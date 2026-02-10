# Comparison With SkipGNN

This project compares GLADIGATOR with SkipGNN using DisGeNET's curated dataset. The comparison evaluates the performance of both models on the same dataset to demonstrate GLADIGATOR's effectiveness.

### Project Overview
- **Dataset**: DisGeNET curated dataset (same as SkipGNN)
- **Objective**: Compare GLADIGATOR's performance against SkipGNN
- **Additional Data**: BioGrid and UniProt data for enhanced graph construction

### 1. Build-Graph
This component builds graph files based on the DisGeNET curated dataset, enhanced with additional sources.

**Key Features:**
- Uses DisGeNET curated dataset (same as SkipGNN)
- Incorporates BioGrid and UniProt for additional information
- Creates graph files optimized for comparison

**Usage:**
```bash
# Build graph with default parameters
python3 build_graph_skipgnn_comparison.py

# Build graph with custom parameters (if available)
python3 build_graph_skipgnn_comparison.py --param value
```

### 2. Run-Model
This component trains and tests GLADIGATOR using the built graph files, then compares results with SkipGNN.

**Comparison Metrics:**
- AUC-ROC
- Precision
- Recall
- F1-score

**Usage:**
```bash
# Run model with default graph file
python3 run_model_skipgnn_comparison.py

# Run model with specific graph file
python3 run_model_skipgnn_comparison.py --graph-file path/to/graph.pt
```

### Project Structure
```
Comparison-SkipGNN/
├── Build_Graph/
│   ├── build_graph_skipgnn_comparison.py  # Graph construction script
│   ├── build-skipgnn-graph.PNG            # Graph construction 
│   └── README.md                          # Build-Graph documentation
├── Run_Model/
│   ├── run_model_skipgnn_comparison.py    # Model training and testing
│   ├── main-algorithm.png                 # Model architecture 
│   ├── README.md                          # Run-Model documentation
│   └── results/                           # Comparison results(auto-generated)
└── README.md                              # Main project documentation
```

### Prerequisites
- Python 3.11
- PyTorch
- NetworkX
- Pandas
- NumPy
- Scikit-learn
- Matplotlib (for visualization)

### Installation
1. Create and activate a virtual environment
2. Install dependencies: `pip install -r requirements.txt`
3. Download and unzip source files from `source-files/` directory
4. Download DisGeNET curated dataset

### Usage Workflow
1. **Build Graph**: Create graph files using DisGeNET curated dataset
2. **Train Model**: Train GLADIGATOR on the constructed graph
3. **Compare Results**: Compare GLADIGATOR's performance with SkipGNN
4. **Analyze**: Generate comparison reports and visualizations

### Data Sources
- **Primary**: DisGeNET curated dataset (same as SkipGNN)
- **Additional**: 
  - BioGrid for gene-gene associations
  - UniProt for protein sequence information

### Expected Results
The comparison should demonstrate:
- GLADIGATOR's superior performance on the same dataset
- Improved accuracy and F1-score
- Better handling of complex relationships
- More efficient training/inference times

### Troubleshooting
- **Dataset Issues**: Ensure DisGeNET curated dataset is properly downloaded
- **Memory Issues**: Reduce batch size if encountering memory errors
- **Comparison Errors**: Verify both models are using the same evaluation metrics
