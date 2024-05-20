import pickle
from model import LogisticRegression

# Training data
X = [
    [1, 2],
    [2, 3],
    [3, 4],
    [4, 5],
    [5, 6]
]
y = [0, 1, 0, 1, 0]

# Train the model
model = LogisticRegression()
model.train(X, y)

# Save the model to a file
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)
