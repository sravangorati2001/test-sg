import pandas as pd
from sklearn.linear_model import LogisticRegression
import pickle

# Load the training data
data = pd.read_csv('data/iris.csv')

# Separate features and target
X = data[['feature1', 'feature2']]
y = data['target']

# Train the model
model = LogisticRegression()
model.fit(X, y)

# Save the model to a file
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)
