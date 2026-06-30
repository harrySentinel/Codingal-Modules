import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline

import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

import warnings
warnings.filterwarnings('ignore')

data = '/kaggle/input/facebook-live-sellers-in-thailand-uci-ml-repo/live.csv'
df = pd.read_csv(data)

df.shape

df.head()

df.info()

df.isnull().sum()

df.drop(['column1', 'column2', 'column3', 'column4'], axis=1, inplace=True)

df.info()

df.describe()

df['status_id'].unique()

len(df['status_id'].unique())

df['status_published'].unique()

len(df['status_published'].unique())

df['status_type'].unique()

len(df['status_type'].unique())

df.drop(['status_id', 'status_published'], axis=1, inplace=True)

df.info()

df.head()

X = df
y = df['status_type']

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
X['status_type'] = le.fit_transform(X['status_type'])
y = le.transform(y)

X.info()

X.head()

cols = X.columns
from sklearn.preprocessing import MinMaxScaler
ms = MinMaxScaler()
X = ms.fit_transform(X)
X = pd.DataFrame(X, columns=[cols])

X.head()

from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=2, random_state=0)
kmeans.fit(X)

kmeans.cluster_centers_

labels = kmeans.labels_
correct_labels = sum(y == labels)
print("Result: %d out of %d samples were correctly labeled." % (correct_labels, y.size))
print('Accuracy score: {0:0.2f}'.format(correct_labels / float(y.size)))

cs = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', max_iter=300, n_init=10, random_state=0)
    kmeans.fit(X)
    cs.append(kmeans.inertia_)
plt.plot(range(1, 11), cs)
plt.title('The Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('Inertia')
plt.show()

kmeans = KMeans(n_clusters=7, random_state=0)
kmeans.fit(X)
labels = kmeans.labels_
