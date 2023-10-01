from RedWineQualityMLProject.constants import *
from RedWineQualityMLProject.utils.common import read_yaml,create_directories
from RedWineQualityMLProject.entity.config_entity import DataIngestionConfig,DataValidationConfig

class ConfigurationManager:
    def __init__(
        self, config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH,
        schema_filepath = SCHEMA_FILE_PATH
    ):
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        self.schema = read_yaml(schema_filepath)
        create_directories([self.config.artifacts_root])
    def get_dataIngestion_config(self)->DataIngestionConfig:
        config = self.config.data_ingestion
        create_directories(config.root_dir)
        dataIngestion_config = DataIngestionConfig(root_dir=config.root_dir,source_URL=config.source_URL,local_data_file=config.local_data_file,unzip_dir=config.unzip_dir)
        return dataIngestion_config
    def get_dataValidation_config(self)->DataValidationConfig:
        config = self.config.data_validation       
        schema = self.schema.COLUMNS
        create_directories(config.root_dir)
        dataValidation_config = DataValidationConfig(root_dir=config.root_dir,unzip_data_dir=config.unzip_data_dir,STATUS_FILE=config.STATUS_FILE, all_schema=schema)
        return dataValidation_config