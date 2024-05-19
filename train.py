import joblib
import pandas as pd
from sklearn import tree

def train():
    # Load dataset
    data = pd.read_csv('data/iris.csv', header=None)
    X, y = data.iloc[:, 1:], data.iloc[:, 0]

    # Train model
    clf = tree.DecisionTreeClassifier(max_leaf_nodes=30)
    clf.fit(X, y)

    # Save model
    joblib.dump(clf, 'model.joblib')

if __name__ == "__main__":
    train()
