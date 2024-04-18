import sys 
import os 
from src.exception import CustomException 
from src.logger import logging 
from src.utils import load_obj
import pandas as pd

class PredictPipeline: 
    def __init__(self) -> None:
        pass

    def predict(self, features): 
        try: 
            preprocessor_path = os.path.join('artifacts', 'preprocessor.pkl')
            model_path = os.path.join("artifacts", "model.pkl")

            preprocessor = load_obj(preprocessor_path)
            model = load_obj(model_path)

            data_scaled = preprocessor.transform(features)
            pred = model.predict(data_scaled)
            return pred
        except Exception as e: 
            logging.info("Error occured in predict function in prediction_pipeline location")
            raise CustomException(e,sys)
        

class CustomData:
    def __init__(self, state: str, district: str, crop: str, year: int, season: str, area: float, production: float):
        self.state = state
        self.district = district
        self.crop = crop
        self.year = year
        self.season = season
        self.area = area
        self.production = production

    def get_data_as_dataframe(self):
        try:
            custom_data_input_dict = {
                'State': [self.state],
                'District': [self.district],
                'Crop': [self.crop],
                'Year': [self.year],
                'Season': [self.season],
                'Area': [self.area],
                'Production': [self.production],
            }
            df = pd.DataFrame(custom_data_input_dict)
            logging.info("Dataframe created")
            return df
        except Exception as e:
            logging.info("Error occurred in get_data_as_dataframe function in prediction_pipeline")
            raise CustomException(e, sys)
