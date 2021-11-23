import sklearn
import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import fetch_olivetti_faces #Fetch the olivetti datasets
from sklearn.model_selection import StratifiedShuffleSplit #Stratify and shuffle splitting the data
from sklearn.decomposition import PCA #Principal Component Analysis
from sklearn.cluster import KMeans 
from sklearn.metrics import silhouette_score #To check for optimal number of clusters

data_olivetti = fetch_olivetti_faces()

data_split = StratifiedShuffleSplit(n_splits=1, test_size=40, random_state= 7)
train_valid, test_valid = next(data_split.split(data_olivetti.data, data_olivetti.target))

x_train_olv = data_olivetti.data[train_valid]
y_train_olv = data_olivetti.target[train_valid]

x_test = data_olivetti.data[test_valid]
y_test = data_olivetti.target[test_valid]

data_split = StratifiedShuffleSplit(n_splits=1, test_size=80, random_state= 7)
trained_data, valid_data = next(data_split.split(x_train_olv, y_train_olv))

x_trained = x_train_olv[trained_data]
y_trained = y_train_olv[trained_data]

x_valid = x_train_olv[valid_data]
y_valid = y_train_olv[valid_data]

pca = PCA(0.99)
x_train_pca = pca.fit_transform(x_trained)
x_tested_pca = pca.transform(x_test)
x_valid_pca = pca.transform(x_valid)

pca.n_components_

# Printing the training data set, validation dataset and the test dataset
#print (x_trained.shape, y_trained.shape)
#print(x_valid.shape, y_valid.shape)
#print (x_test.shape, y_test.shape)

k_range = range(5, 150, 5)
kmeans_per_k = []
for k in k_range:
    #print('K={}'.format(k))
    kmeans = KMeans(n_clusters=k, random_state= 7).fit(x_train_pca)
    kmeans_per_k.append(kmeans)

slht_scores = [silhouette_score(x_train_pca, model.labels_)
                for model in kmeans_per_k]

best_cluster_value = np.argmax(slht_scores)
best_k_value = k_range[best_cluster_value]
best_slht_score = slht_scores[best_cluster_value]
best_model = kmeans_per_k[best_cluster_value]

print(best_cluster_value, best_k_value, best_slht_score, best_model)
