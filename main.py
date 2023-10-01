from RedWineQualityMLProject import logger
# logger.info("Welcome to our custom logging")
from RedWineQualityMLProject.pipeline.stage_01_dataingestion import DataIngestionPipeline
from RedWineQualityMLProject.pipeline.stage_02_datavalidation import DataValidationPipeline
from RedWineQualityMLProject.pipeline.stage_03_datatransformation import DataTransformationPipeline
STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info("f>>>> stage {STAGE_NAME} started <<<<")
    data_ingestion = DataIngestionPipeline()
    data_ingestion.main()
    logger.info(f">>>>stage {STAGE_NAME} completed <<<<\n\nx======x")
except Exception as e:
    logger.exception(e)
    raise e
STAGE_NAME = "Data Validation Stage"
try:
    logger.info("f>>>> stage {STAGE_NAME} started <<<<")
    data_validation = DataValidationPipeline()
    data_validation.main()
    logger.info(f">>>>stage {STAGE_NAME} completed <<<<\n\nx======x")
except Exception as e:
    logger.exception(e)
    raise e
STAGE_NAME = "Data Transformation Stage"
try:
    logger.info("f>>>> stage {STAGE_NAME} started <<<<")
    data_transformation = DataTransformationPipeline()
    data_transformation.main()
    logger.info(f">>>>stage {STAGE_NAME} completed <<<<\n\nx======x")
except Exception as e:
    logger.exception(e)