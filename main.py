from src.mlproject.logger import logging
from src.mlproject.exception import CustomException
import sys
from src.mlproject.components.data_ingestion import DataIngestion
from src.mlproject.components.data_ingestion import DataIngestionConfig
from src.mlproject.components.data_transformation import DataTransformation
from src.mlproject.components.model_tranier import ModelTrainer
from src.mlproject.components.model_tranier import ModelTrainerConfig

if __name__ == '__main__':
    logging.info('Running')
    try:
        
       data_ingestion=DataIngestion()
       train_path,test_path = data_ingestion.initiate_data_ingestion()
       data_transformation = DataTransformation()
       train_arr, test_arr,_ = data_transformation.initiate_data_transformation(train_path,test_path)
       
       model_trainer=ModelTrainer()
       print(model_trainer.initiate_model_trainer(train_arr, test_arr))
    
    except Exception as e:
        logging.info('Exception')
        raise CustomException(e,sys) 