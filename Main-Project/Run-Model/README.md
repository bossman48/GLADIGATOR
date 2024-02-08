# Run-Model

In this part, our deep learning model is trained and tested. Steps' of the train/test process is mentioned in below.

<p align="center"> 
    <img src="run-model.png">
</p>

## Input Parameter
Only input parameter is a path of the graph file that is a dataset model is trained/tested on this dataset.

### Example Usages
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