# Run-Model

In this part, our deep learning model is trained and tested. Steps' of the train/test process is mentioned in below.

<p align="center"> 
    <img src="run-model.png">
</p>

## Input Parameter
Only input parameter is a path of the graph file that is a dataset model is trained/tested on this dataset.

### Example Usages
For example, you want run model with grapt that is build based on OGB's ogbl-biokg dataset, you can call this command.

```
    python3 run_model_ogb_comparison.py "../../graph-files/Graph_Comparison_OGB.pt"
```

:warning:

In your machine you can call ***python*** instead of ***python3*** 

## Output Files

After train model operation is completed. Best validation and test result is stored in a csv file.

---

For example, you run this command, that is mentioned in below.
```
    python3 run_model_ogb_comparison.py "../../graph-files/Graph_Comparison_OGB.pt"
```

End of the train process, the best validation and test result are store in ***val-resultsGraph_Comparison_OGB.csv*** and ***test-resultsGraph_Comparison_OGB.csv***
