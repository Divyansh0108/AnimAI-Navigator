from src.data_loader import AnimeDataLoader
from src.vector_store import VectorStoreBuilder
from dotenv import load_dotenv
from utils.logger import get_logger 
from utils.custom_exception import CustomException

load_dotenv()
logger = get_logger()

def main():
    try:
        logger.info("Starting the build pipeline...")

        loader = AnimeDataLoader("data/anime_with_synopsis.csv", "data/processed_anime_data.csv")
        processed_csv = loader.load_and_process()
        logger.info("Data loaded and processed...")

        vector_builder = VectorStoreBuilder(processed_csv)
        vector_builder.build_and_save_vectorstore()

        logger.info("Vector store built and saved successfully.")
        
        logger.info("Build pipeline completed successfully.")

    except Exception as e:
        logger.error(f"Error occurred during build pipeline: {e}")
        raise CustomException("Build pipeline failed") from e


if __name__ == "__main__":
    main()