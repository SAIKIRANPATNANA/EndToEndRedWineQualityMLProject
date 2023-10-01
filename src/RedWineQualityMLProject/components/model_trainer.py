import pandas as pd
import pickle as pkl
import os
from RedWineQualityMLProject import logger
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from RedWineQualityMLProject.config.configuration import ModelTrainerConfig
class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config
    def train(self):
        train_data = pd.read_csv(self.config.train_data_path)
        test_data = pd.read_csv(self.config.test_data_path)
        x_train = train_data.drop(self.config.target_column, axis=1)
        x_test = test_data.drop(self.config.target_column, axis=1)
        y_train = train_data[self.config.target_column]
        y_test = test_data[self.config.target_column]
        std_scaler = StandardScaler()
        x_train = std_scaler.fit_transform(x_train)
        x_test = std_scaler.transform(x_test)
        rfr = RandomForestRegressor()
        rfr.fit(x_train,y_train)
        with open(os.path.join(self.config.root_dir[0], self.config.model_name), 'wb') as f:
            pkl.dump(rfr, f)
        
        
        



