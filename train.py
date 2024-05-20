from sklearn.tree import DecisionTreeClassifier
import pickle

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
model = DecisionTreeClassifier()
model.fit(X, y)

# Save the model to a file
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)
