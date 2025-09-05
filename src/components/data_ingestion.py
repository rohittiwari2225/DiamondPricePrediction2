#I am writing comment for each line of code
import os# Importing the os module to interact with the operating system
import sys# Importing the sys module to access system-specific parameters and functions
from src.logger import logging# Importing the logging module from the src.logger package for logging purposes
from src.exception import CustomException# Importing the CustomException class from the src.exception package for
import pandas as pd# Importing the pandas library for data manipulation and analysis
from sklearn.model_selection import train_test_split# Importing the train_test_split function from sklearn for splitting data into training and testing sets
from dataclasses import dataclass# Importing the dataclass decorator from the dataclasses module to create data classes

## initializing the data ingestion configuration using dataclass
@dataclass
class DataIngestionConfig:
    train_data_path=os.path.join('artifacts','train.csv')# Path to save the training data
    test_data_path=os.path.join('artifacts','test.csv')# Path to save the testing data
    raw_data_path=os.path.join('artifacts','data.csv')# Path to save the raw data

# creating a class for data ingestion
class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()# Initializing the data ingestion configuration

    def initiate_data_ingestion(self):
        logging.info("Data Ingestion method starts")

        try:
            df=pd.read_csv('notebooks/data/gemstone.csv')# Reading the dataset from a CSV file
            logging.info("Dataset read as pandas dataframe")
            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path),exist_ok=True)# Creating the directory to save the data if it doesn't exist
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)# Saving the raw data to a CSV file
            logging.info("Train test split initiated")
            train_set,test_set=train_test_split(df,test_size=0.3,random_state=42)# Splitting the data into training and testing sets
            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)# Saving the training data to a CSV file
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)# Saving the testing data to a CSV file
            logging.info("Ingestion of data is completed")
            return (self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path)
            # Returning the paths of the training and testing data files

        except Exception as e:
            logging.info("Exception occured at data ingestion stage")
        