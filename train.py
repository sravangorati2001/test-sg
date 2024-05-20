import pandas as pd
from sklearn.linear_model import LogisticRegression
import pickle

data = pd.read_csv('data/iris.csv')


X = data.iloc[:, :-1]
y = data.iloc[:, -1]

model = LogisticRegression()
model.fit(X, y)

with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)
