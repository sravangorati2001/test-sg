import pandas as pd
from sklearn.linear_model import LogisticRegression
import pickle

# Load the dataset
data = pd.read_csv('data/iris.csv')

# Assume the dataset has features in columns 0 to -1 and target in the last column
X = data.iloc[:, :-1]
y = data.iloc[:, -1]

# Train the model
model = LogisticRegression()
model.fit(X, y)

# Save the model
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)
