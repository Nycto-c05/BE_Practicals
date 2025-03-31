import json
import os
import kaggle
import pandas as pd

def data_loading():
  # Define the path to kaggle.json
  kaggle_json_path = "./kaggle.json" #make sure to put correct file path

  # Load the JSON file
  with open(kaggle_json_path, "r") as f:
      kaggle_credentials = json.load(f)

  # Set environment variables
  os.environ["KAGGLE_USERNAME"] = kaggle_credentials["username"]
  os.environ["KAGGLE_KEY"] = kaggle_credentials["key"]
  

  # Verify
  print("Kaggle credentials set successfully!")


  kaggle.api.dataset_download_files(
      'vanvalkenberg/historicalweatherdataforindiancities',
      path='.',
      unzip=True
  )

  weather_data = pd.read_csv("./Temperature_And_Precipitation_Cities_IN/Mumbai_1990_2022_Santacruz.csv")

  return weather_data


