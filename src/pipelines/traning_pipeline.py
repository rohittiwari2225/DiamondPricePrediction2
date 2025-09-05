import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
import pandas as pd
from src import components
from src.logger import logging
from src.exception import CustomException
from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_traner import ModelTrainer

if __name__=="__main__":
    obj=DataIngestion()# Creating an instance of the DataIngestion class
    train_data_path,test_data_path=obj.initiate_data_ingestion()# Initiating the data ingestion process and getting the paths of the training and testing data files
    print(train_data_path,test_data_path)# Printing the paths of the training and testing data files
  
    data_transformation=DataTransformation()# Creating an instance of the DataTransformation class
   
    train_arr,test_arr,_ =data_transformation.initiate_data_transformation(train_data_path,test_data_path)# Initiating the data transformation process using the training and testing data file paths  
    
    model_trainer=ModelTrainer()
    model_trainer.initiate_model_trainer(train_arr,test_arr)