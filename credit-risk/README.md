# Running the model `default_risk_random_forest_only.ipynb`


## To get the data into Dotscience

1. Add the notebook and the file `application_test.csv`  via the GUI **Resources** uploader. We'll get the data from Kaggle's API as its too big to get into Dotscience via the GUI uploader right now.

2. Start Jupyter, and open up a terminal. If you are working in a new project, or have powered your runner off in an existing project since you last used it, you should paste in the following:

(keep this relatively private as it contains an API key)

```
pip install seaborn kaggle &&\
   mkdir -p ~/.kaggle &&\
   echo "{\"username\":\"hodesdon\",\"key\":\"dff06e16436b47c14634841335acb032\"}" > ~/.kaggle/kaggle.json &&\ 
   kaggle datasets download -d julianocosta/home-credit &&\
   unzip home-credit 

```

3. Navigate to notebook and run all cells as usual. 

* For demo, you can vary the number of trees using the `n_estimators ` parameter.

* The metric returned is the [out of bag score](https://en.wikipedia.org/wiki/Out-of-bag_error)

* The slowest parts to run are plotting the correlation matrix (under heading **Correlation between features**) and fitting the model.

## To speed up model
1. Use a VM with with 8 CPUs, 40 GB memory (or more). Keep the `n_cores` parameter on the `.fit()` method of the random forest classifier set to `-1` to take advantage of paralellism in training. 

2. Decrease the number of trees (`n_estimators`) to speed up training:

| `n_estimators` 	| approx time to train model on 8CPUs, 40GB RAM 	|
|----------------	|-----------------------------------------------	|
| 10             	| 10.5s                                         	|
| 100            	| 1.5m                                          	|
| 1000           	| 15min                                         	|

## Caveats
At the moment, although we load in 6 data files, only one of them (`application_test.csv`) actually features in the dataframe. The rest just get declared as imputs but not read. We could do something with this extra data for a more complex demo in the future. Or, if the provenance graph looks too messy, just drop one of the inputs.