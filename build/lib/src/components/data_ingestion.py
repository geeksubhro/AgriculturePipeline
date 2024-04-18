import os
import sys
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from src.logger import logging
from src.exception import CustomException

@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifacts', 'train.csv')
    test_data_path: str = os.path.join('artifacts', 'test.csv')
    raw_data_path: str = os.path.join('artifacts', 'raw.csv')

class DataIngestion:
    def __init__(self):
        self.config = DataIngestionConfig()
    
    def initiate_data_ingestion(self):
        try:
            logging.info('Starting data ingestion')

            # Load agricultural data from CSV
            agri_data = self._load_data(os.path.join('notebooks/data', 'agri.csv'))
            logging.info('Dataset loaded successfully')

            # Preprocess data
            tonnes_data = self._preprocess_data(agri_data)

            # Save raw data
            self._save_raw_data(agri_data)

            # Perform train-test split
            self._perform_train_test_split(tonnes_data)

            logging.info('Data ingestion completed successfully')
            return (self.config.train_data_path, self.config.test_data_path)

        except FileNotFoundError as e:
            logging.error(f'File not found: {e.filename}')
            raise CustomException(f'File not found: {e.filename}', sys)
        except Exception as e:
            logging.error(f'Error occurred during data ingestion: {str(e)}')
            raise CustomException(str(e), sys)

    def _load_data(self, file_path):
        """Load agricultural data from CSV."""
        return pd.read_csv(file_path)

    def _preprocess_data(self, df):
        """Preprocess the data."""
        tonnes_data = df[df['Production Units'] == 'Tonnes'].copy()
        tonnes_data.reset_index(drop=True, inplace=True)
        df.drop(columns=['Production Units', 'Area Units'], inplace=True)
        
        # Use .loc to modify the DataFrame
        df.loc[:, 'Year'] = df['Year'].str.replace(r'^(\d{4})-\d{2}$', r'\1', regex=True)
        tonnes_data.loc[:, 'Year'] = tonnes_data['Year'].str.replace(r'^(\d{4})-\d{2}$', r'\1', regex=True)
        
        return tonnes_data


    def _save_raw_data(self, df):
        """Save raw data to file."""
        os.makedirs(os.path.dirname(self.config.raw_data_path), exist_ok=True)
        df.to_csv(self.config.raw_data_path, index=False)
        logging.info('Raw data saved to file')

    def _perform_train_test_split(self, df):
        """Perform train-test split."""
        train_set, test_set = train_test_split(df, test_size=0.30, random_state=42)
        train_set.to_csv(self.config.train_data_path, index=False, header=True)
        test_set.to_csv(self.config.test_data_path, index=False, header=True)
        logging.info('Train-test split completed')
