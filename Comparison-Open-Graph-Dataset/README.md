# GLADIGATOR vs OGB Benchmark: Performance Comparison

## Overview
This project compares GLADIGATOR with other methods using the Open Graph Benchmark (OGB) ***ogbl-biokg*** dataset. The comparison evaluates GLADIGATOR's performance on a standardized benchmark dataset.

### Project Overview
- **Dataset**: OGB ***ogbl-biokg*** (Open Graph Benchmark for biological knowledge graphs)
- **Objective**: Compare GLADIGATOR's performance against other methods on a standardized benchmark
- **Additional Data**: BioGrid and UniProt data for enhanced graph construction

### Project Overview
- **Dataset**: OGB ***ogbl-biokg*** (Open Graph Benchmark for biological knowledge graphs)
- **Objective**: Compare GLADIGATOR's performance against other methods on a standardized benchmark
- **Additional Data**: BioGrid and UniProt data for enhanced graph construction

### 1. Build-Graph
This component builds graph files based on the OGB ***ogbl-biokg*** dataset, enhanced with additional sources.

**Key Features:**
- Uses OGB ***ogbl-biokg*** dataset (standardized benchmark)
- Incorporates BioGrid and UniProt for additional information
- Creates graph files optimized for comparison with other methods

**Key Features:**
- Uses OGB ***ogbl-biokg*** dataset (standardized benchmark)
- Incorporates BioGrid and UniProt for additional information
- Creates graph files optimized for comparison with other methods

**Usage:**
```bash
# Build graph with default parameters
python3 build_graph_ogb_comparison.py

# Build graph with custom parameters (if available)
python3 build_graph_ogb_comparison.py --param value
```

### 2. Run-Model
This component trains and tests GLADIGATOR using the built graph files, then compares results with other methods on the OGB benchmark.

### 2. Run-Model
This component trains and tests GLADIGATOR using the built graph files, then compares results with other methods on the OGB benchmark.

**Comparison Metrics:**
- OGB evaluation metrics (hits@10, hits@50, mrr)
- AUC-ROC
- Precision
- Recall
- F1-score
- Training time
- Inference time

**Usage:**
```bash
# Run model with default graph file
python3 run_model_ogb_comparison.py

# Run model with specific graph file
python3 run_model_ogb_comparison.py --graph-file path/to/graph.pt
```

### Project Structure
```
Comparison-Open-Graph-Dataset/
├── Build_Graph/
│   ├── build_graph_ogb_comparison.py  # Graph construction script
│   ├── build-ogb-graph.PNG            # Graph construction visualization
│   └── README.md                      # Build-Graph documentation
├── Run_Model/
│   ├── run_model_ogb_comparison.py    # Model training and testing
│   ├── main-algorithm.png             # Model architecture visualization
│   ├── README.md                      # Run-Model documentation
│   └── results/                       # Comparison results (auto-generated)
└── README.md                          # Main project documentation
```

**Usage:**
```bash
# Run model with default graph file
python3 run_model_ogb_comparison.py

# Run model with specific graph file
python3 run_model_ogb_comparison.py --graph-file path/to/graph.pt
```

### Project Structure
```
Comparison-Open-Graph-Dataset/
├── Build_Graph/
│   ├── build_graph_ogb_comparison.py  # Graph construction script
│   ├── build-ogb-graph.PNG            # Graph construction visualization
│   └── README.md                      # Build-Graph documentation
├── Run_Model/
│   ├── run_model_ogb_comparison.py    # Model training and testing
│   ├── main-algorithm.png             # Model architecture visualization
│   ├── README.md                      # Run-Model documentation
│   └── results/                       # Comparison results (auto-generated)
└── README.md                          # Main project documentation
```

### Prerequisites
- Python 3.11
- PyTorch
- NetworkX
- Pandas
- NumPy
- Scikit-learn
- OGB library
- Matplotlib (for visualization)

### Installation
1. Create and activate a virtual environment
2. Install dependencies: `pip install -r requirements.txt`
3. Install OGB: `pip install ogb`
4. Download and unzip source files from `source-files/` directory
5. Download OGB ***ogbl-biokg*** dataset

### Usage Workflow
1. **Build Graph**: Create graph files using OGB ***ogbl-biokg*** dataset
2. **Train Model**: Train GLADIGATOR on the constructed graph
3. **Compare Results**: Compare GLADIGATOR's performance with other methods
4. **Analyze**: Generate comparison reports and visualizations

### Data Sources
- **Primary**: OGB ***ogbl-biokg*** dataset (standardized benchmark)
- **Additional**:
  - BioGrid for gene-gene associations
  - UniProt for protein sequence information

### Expected Results
The comparison should demonstrate:
- GLADIGATOR's superior performance on the standardized benchmark
- Improved accuracy and F1-score compared to other methods
- Better handling of complex relationships in biological knowledge graphs
- Competitive performance on OGB evaluation metrics

### Troubleshooting
- **Dataset Issues**: Ensure OGB ***ogbl-biokg*** dataset is properly downloaded
- **Memory Issues**: Reduce batch size if encountering memory errors
- **Comparison Errors**: Verify all methods are using the same evaluation metrics

### Installation
1. Create and activate a virtual environment
2. Install dependencies: `pip install -r requirements.txt`
3. Install OGB: `pip install ogb`
4. Download and unzip source files from `source-files/` directory
5. Download OGB ***ogbl-biokg*** dataset

### Usage Workflow
1. **Build Graph**: Create graph files using OGB ***ogbl-biokg*** dataset
2. **Train Model**: Train GLADIGATOR on the constructed graph
3. **Compare Results**: Compare GLADIGATOR's performance with other methods
4. **Analyze**: Generate comparison reports and visualizations

### Data Sources
- **Primary**: OGB ***ogbl-biokg*** dataset (standardized benchmark)
- **Additional**: 
  - BioGrid for gene-gene associations
  - UniProt for protein sequence information

### Expected Results
The comparison should demonstrate:
- GLADIGATOR's superior performance on the standardized benchmark
- Improved accuracy and F1-score compared to other methods
- Better handling of complex relationships in biological knowledge graphs
- Competitive performance on OGB evaluation metrics

### Troubleshooting
- **Dataset Issues**: Ensure OGB ***ogbl-biokg*** dataset is properly downloaded
- **Memory Issues**: Reduce batch size if encountering memory errors
- **Comparison Errors**: Verify all methods are using the same evaluation metrics
