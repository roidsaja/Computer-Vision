# Common imports
import os
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.rc('axes', labelsize=14)
mpl.rc('xtick', labelsize=12)
mpl.rc('ytick', labelsize=12)

from sklearn.datasets import fetch_openml
mnist = fetch_openml('mnist_784', version=1, as_frame=False)
# print(mnist.keys())

X, y = mnist["data"], mnist["target"]
# print(X.shape)
# print(y.shape)

some_digit = X[0]
some_digit_image = some_digit.reshape(28, 28)

X_train, X_test, y_train, y_test = X[:600], X[600:], y[:600], y[600:]

# plt.imshow(some_digit_image, cmap="binary")
# plt.axis("off")
# plt.show()

# 1. Try to build a classifier for the MNIST dataset that achieves over
# 97% accuracy on the test set. Hint: the KNeighborsClassifier
# works quite well for this task; you just need to find good
# hyperparameter values (try a grid search on the weights and
# n_neighbors hyperparameters).

from sklearn.model_selection import GridSearchCV
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

param_grid = [{
    'weights': ['uniform', 'distance'], 
    'n_neighbors': [3, 4, 5],
}]

knn_clf = KNeighborsClassifier()
grid_search = GridSearchCV(knn_clf, param_grid, cv=5, verbose=3, n_jobs=-1)
grid_search.fit(X_train, y_train)

y_pred = grid_search.predict(X_test)

print(grid_search.best_params_)
print(grid_search.best_score_)
print('Y Predict: ', y_pred)
print('Accuracy Score: ', accuracy_score(y_test, y_pred))