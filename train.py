import math
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

class LogisticRegression:
    def __init__(self):
        self.weights = [0.0 for _ in range(len(X[0]) + 1)]
    
    def sigmoid(self, z):
        return 1 / (1 + math.exp(-z))
    
    def predict(self, X):
        predictions = []
        for row in X:
            z = self.weights[0] + sum(w * x for w, x in zip(self.weights[1:], row))
            predictions.append(1 if self.sigmoid(z) >= 0.5 else 0)
        return predictions
    
    def train(self, X, y, epochs=1000, lr=0.1):
        for _ in range(epochs):
            for row, target in zip(X, y):
                z = self.weights[0] + sum(w * x for w, x in zip(self.weights[1:], row))
                prediction = self.sigmoid(z)
                error = target - prediction
                self.weights[0] += lr * error
                for i in range(len(row)):
                    self.weights[i + 1] += lr * error * row[i]

# Train the model
model = LogisticRegression()
model.train(X, y)

# Save the model to a file
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)
