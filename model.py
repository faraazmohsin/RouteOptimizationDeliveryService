# Unzip contents from the rounD Dataset from Google Drive
import zipfile
import os
import pandas as pd

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

zip_path = '/content/drive/MyDrive/rounD-dataset-v1.0.zip'

with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall('/content/drive/MyDrive/rounD-dataset')
    
#---------------------------------------------------------------#

os.chdir('/content/drive/MyDrive/rounD-dataset/data')

# Empty arrays to store the dataframes
df_recordingMeta = []
df_tracks = []
df_tracksMeta = []

# for loop for file names and loading the CSV files into dataframes
for i in range(3):
    # format the file name with leading zeros
    file_num = str(i).zfill(2)
    file_prefix = file_num + "_"
    
       # load the CSV files into dataframes
    df_recordingMeta.append(pd.read_csv(file_prefix + 'recordingMeta.csv'))
    df_tracks.append(pd.read_csv(file_prefix + 'tracks.csv'))
    df_tracksMeta.append(pd.read_csv(file_prefix + 'tracksMeta.csv'))
    
# concatenate the dataframes
df_recordingMeta = pd.concat(df_recordingMeta, ignore_index=True, axis=0)
df_tracks = pd.concat(df_tracks, ignore_index=True, axis=0)
df_tracksMeta = pd.concat(df_tracksMeta, ignore_index=True, axis=0)

# check for null values
print(df_recordingMeta.isnull().sum())
print(df_tracks.isnull().sum())
print(df_tracksMeta.isnull().sum())

#---------------------------------------------------------------#

# merge the dataframes into one dataframe based on a common column
df_merged = pd.merge(df_recordingMeta, df_tracks, on='recordingId')
df_merged = pd.merge(df_merged, df_tracksMeta, on='trackId')

# define X and y, we're defining features and target variable based on columns from dataset
X = df_merged[['speedLimit', 'xCenter', 'yCenter']]
y = df_merged['class']

# handle outliers by replacing with median values
X_median = X.median()
X = X.fillna(X_median)
X = X.mask((X.sub(X_median).div(X.std()).abs().gt(3)), other=X_median, axis=1)

# split the data into training, validation, and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=0.25, random_state=42)

# training of KNN model
k = 5
knn = KNeighborsClassifier(n_neighbors=k)
knn.fit(X_train, y_train)

# validation
y_val_pred = knn.predict(X_val)
val_accuracy = accuracy_score(y_val, y_val_pred)
print(f"Validation accuracy: {val_accuracy}")

# test
y_test_pred = knn.predict(X_test)
test_accuracy = accuracy_score(y_test, y_test_pred)
print(f"Test accuracy: {test_accuracy}")