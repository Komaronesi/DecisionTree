import numpy as np
from sklearn.datasets import make_regression, make_classification
from sklearn.model_selection import train_test_split


X, y = make_classification()

class DecisionTreeClassifier():

    def __init__(self, max_depth = 10, criterion = 'gini', min_samples_leaf = 2):
        self.max_depth = max_depth
        self.criterion = criterion
        self.min_samples_leaf = min_samples_leaf
        pass

    def fit(self, X, y):
        tree = self.grow_tree(X, y, current_depth = 0)
        pass

    def predict(self, X):

        return preds
        pass

    def grow_tree(self, X, y, current_depth):
        splits = self.get_best_splits(X, y)

    def get_best_splits(self, X, y):
        splits = []
        best_entropy = 0
        for i in X.shape[1]:


    def entropy(self, X, y):
        entropy_ = 0
        for yi in y.unique():
            entropy_ += y[y == yi]
        pass

    def gini(self, X, y):
        pass


