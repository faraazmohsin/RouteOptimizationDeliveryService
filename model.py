# Unzip contents from the rounD Dataset
import zipfile
import os

zip_path = '/content/drive/MyDrive/rounD-dataset-v1.0.zip'

with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall('/content/drive/MyDrive/rounD-dataset')