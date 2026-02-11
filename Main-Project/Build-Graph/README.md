# Build-Graph: Graph Construction

## Overview
This component builds customizable graph files from gathered sources including DisGeNET, BioGrid, and UniProt. The graphs are constructed based on gene-disease associations with customizable score thresholds.

### Key Features:
- Creates graph files with different gene-disease score thresholds
- Incorporates multiple data sources for comprehensive graph construction
- Generates files in PyTorch format for model training

<p align="center">
    <img src="build-main-graph.png">
</p>

## Input Parameter
Only input parameter is gene-disease score threshold.

### Example Usages
For example, you want build a graph that gene-disease score is equal and more that 0.5, you can run this command.

```
    python3 build_graph.py 0.5
```

Another example, you want build a graph that gene-disease score is equal and more that 0.1, you can run this command.

```
    python3 build_graph.py 0.1
```

Another example, you want build a graph that gene-disease score is equal and more that 0.05, you can run this command.

```
    python3 build_graph.py 0.05
```

## Important Notes
- ***python*** keyword is used to call ***python3*** in some machines. If your machine is like that, you can change ***python3*** keyword with ***python*** keyword.
