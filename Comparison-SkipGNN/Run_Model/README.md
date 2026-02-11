# Run-Model: Model Training and Testing

## Overview
This component trains and tests GLADIGATOR using the built graph files, then compares results with SkipGNN.

### Model Architecture
The model uses a graph neural network architecture with:
- Node embeddings for genes and diseases
- Edge features for associations
- Attention mechanisms for relationship learning

<p align="center">
    <img src="model-structure.png">
</p>

***Figure 1***: Visualization of the graph neural network architecture showing node embeddings, edge features, and attention mechanisms for gene-disease association prediction.

## Input Parameter
Only input parameter is a path of the graph file that is a dataset model is trained/tested on this dataset.

### Example Usages
For example, you want run model with graph that is build based on DisGeNET curated dataset, you can call this command.

```
    python3 run_model_skipgnn_comparison.py "../../graph-files/Graph_Comparison_SkipGNN.pt"
```

## Important Notes
- ***python*** keyword is used to call ***python3*** in some machines. If your machine is like that, you can change ***python3*** keyword with ***python*** keyword.

## Output Files
After train model operation is completed, the best validation and test results are stored in CSV files.

### Example Output Files
For example, if you run this command:
```
    python3 run_model_skipgnn_comparison.py "../../graph-files/Graph_Comparison_SkipGNN.pt"
```

End of the train process, the best validation and test results are stored in:
- `val-resultsGraph_Comparison_SkipGNN.csv`
- `test-resultsGraph_Comparison_SkipGNN.csv`
