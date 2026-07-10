import os 
import kaggle
dataset = "thedevastator/airbnb-prices-in-european-cities"
download_folder = "./bronze_layer"
kaggle.api.dataset_download_files(dataset, path=download_folder, unzip=True)