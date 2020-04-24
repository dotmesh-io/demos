import numpy as np

def predict(model, query):
    inputs = np.array(query)
    return {"hello": sum(query["instances"][0])}