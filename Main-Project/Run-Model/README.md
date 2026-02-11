# Run-Model: Model Training and Testing

## Overview
This component trains and tests the deep learning model using the built graph files.

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
For example, you want run model with min gene-disease score is 0.5, you can call this command.
```
    python3 run_model.py "../../graph-files/Graph_Own_0.5.pt"
```

Another example, you want run model with min gene-disease score is 0.1, you can call this command.
```
    python3 run_model.py "../../graph-files/Graph_Own_0.1.pt"
```

Another example, you want run model with min gene-disease score is 0.05, you can call this command.
```
    python3 run_model.py "../../graph-files/Graph_Own_0.05.pt"
```

## Important Notes
- ***python*** keyword is used to call ***python3*** in some machines. If your machine is like that, you can change ***python3*** keyword with ***python*** keyword.

## Output Files
After train model operation is completed, the best validation and test results are stored in CSV files.

### Example Output Files
For example, if you run this command:
```
    python3 run_model.py "../../graph-files/Graph_Own_0.5.pt"
```

End of the train process, the best validation and test results are stored in:
- `val-resultsGraph_Own_0.5.csv`
- `test-resultsGraph_Own_0.5.csv`

### Additional Output Files
- `val-resultsGraph_Own_0.1.csv` and `test-resultsGraph_Own_0.1.csv`
- `val-resultsGraph_Own_0.05.csv` and `test-resultsGraph_Own_0.05.csv`
- `val-resultsGraph_Own_0.9.csv` and `test-resultsGraph_Own_0.9.csv`