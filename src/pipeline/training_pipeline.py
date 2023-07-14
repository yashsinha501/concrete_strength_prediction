from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer



if __name__ =="__main__":

    #Data Ingestion
    obj = DataIngestion()
    train_data_path , test_data_path = obj.initiate_data_ingestion()
    #Data Transformation
    data_transform = DataTransformation()
    train_arr, test_arr, _ = data_transform.initiate_data_transformation(train_data_path , test_data_path)
    #Model Training
    modeltrainer = ModelTrainer()
    modeltrainer.initiate_model_trainer(train_arr, test_arr)