# Unzip contents from the rounD Dataset from Google Drive
import zipfile
import os
import pandas as pd

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