#!/usr/bin/python3

from sklearn import datasets
import pandas as pd

data = datasets.load_iris()
X = pd.DataFrame(data["data"], columns=data["feature_names"])
y = pd.Series(data["target"], name="target").map({i:v for i, v in enumerate(data["target_names"])})
train = X.copy()
train["target"] = y

train.to_csv("../../data/raw/train.csv", index=False)
