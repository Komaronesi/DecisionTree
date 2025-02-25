# Decision tree algorithm
This repo represents decision tree algorithms (for regression and classification), made from scratch
feel free to leave some comments and improvements

This repo only relies on numpy for routines and scikit-learn for tests and data loading routines.
Unlike scikit-learn's realisation of DecisionTree, this only supports a few attributes:
|Supported attribute|data type|
|---|---|
|max_depth|int|
|criterion|str, for classfification: ['gini', 'entropy'], for regression: ['MAE', 'MSE']|
|min_samples_leaf|int|
