# Running the model `default_risk_random_forest_only.ipynb`


## To get the data into Dotscience

(keep private-ish -- API key contained below :/)

Open a terminal in Dotscience's Jupyterlab interface. We'll get the data from Kaggle's API as its too big to get into Dotscience via the GUI uploader.

```
pip install seaborn kaggle &&\
   mkdir -p ~/.kaggle &&\
   echo "{\"username\":\"hodesdon\",\"key\":\"dff06e16436b47c14634841335acb032\"}" > ~/.kaggle/kaggle.json &&\ 
   kaggle datasets download -d julianocosta/home-credit &&\
   unzip home-credit 

```

## To run notebook

Run all cells as usual. 

## To speed up model
1. Use a VM with 4 cores

2. change number of trees:
for 100 trees, on 4 cpus, takes about 1.6 minutes