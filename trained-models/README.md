# Trained Models For Make Predictions

In this part, our trained deep learning model is saved. If you can make prediction using our trained models. Steps' of the making prediciton is mentioned in below.


## Input Parameter
Input parameter are mentioned in below.

    1. Trained Model Path: You give the path of the trained model path. Use only models paths.

    2. Gene Symbol: You give the gene smybol as second input.

    3. Disease CUI: You give the disease cui id as third input.


### Example Usages
For example, you want to make prediction between gene HPSE and disease C0001432 via using Graph_Own_0.5_model.pth trained model. You should call this command
```
    python3 MakePrediction.py Graph_Own_0.5_model.pth PRPH2 C0016529
```

For example, you want to make prediction between gene AGER and disease C1518922 via using Graph_Own_0.05_model.pth trained model. You should call this command

```
    python3 MakePrediction.py Graph_Own_0.05_model.pth PRPH2 C0016529
```


:warning:

***python*** keyword is used to call ***python3*** in some machines. If your machine is like that, you can change ***python3*** keyword with ***python*** keyword.
