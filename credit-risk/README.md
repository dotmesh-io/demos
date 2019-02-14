# Running the model `default_risk_random_forest_only.ipynb`


## To get the data into Dotscience

(keep private-ish -- API key contained below :/)

Open a terminal.
```
pip install kaggle \
   mkdir ~/.kaggle
   echo "{"username":"hodesdon","key":"bc83ba268ce3695b369815a227d0991b"}" ~/.kaggle/kaggle.json \
   kaggle datasets download -d julianocosta/home-credit \
   unzip home-credit 

```
## To speed up model
1. Use a VM with 4 cores

2. change number of trees:
for 100 trees, on 4 cpus, takes about 1.6 minutes