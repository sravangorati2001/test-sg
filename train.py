import joblib
import pandas as pd
from sklearn import tree
from sklearn.preprocessing import LabelEncoder

def train():
    # Load dataset
    data = pd.read_csv('data/iris.csv', header=None)
    X, y = data.iloc[:, :-1], data.iloc[:, -1]
    
    # Encode labels
    label_encoder = LabelEncoder()
    y = label_encoder.fit_transform(y)

    # Train model
    clf = tree.DecisionTreeClassifier(max_leaf_nodes=30)
    clf.fit(X, y)

    # Save model and label encoder
    joblib.dump(clf, 'model.joblib')
    joblib.dump(label_encoder, 'label_encoder.joblib')

if __name__ == "__main__":
    train()
