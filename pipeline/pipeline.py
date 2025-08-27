import os
from src.vector_store import VectorStoreBuilder
from src.recommender import AnimeRecommender
from configs.config import GROQ_API_KEY, MODEL_NAME
from utils.logger import get_logger
from utils.custom_exception import CustomException

logger = get_logger()

class AnimeRecommendationPipeline:
    def __init__(self, persist_dir="chroma_db"):
        try:
            logger.info("Initializing Recommendation Pipeline...")
            
            if not os.path.exists(persist_dir):
                logger.error(f"Vector store not found at {persist_dir}. Please run build_pipeline.py first.")
                raise FileNotFoundError(f"Vector store not found at {persist_dir}")
            
            csv_path = "data/processed_anime_data.csv"
            if not os.path.exists(csv_path):
                logger.error(f"Processed CSV not found at {csv_path}. Please run build_pipeline.py first.")
                raise FileNotFoundError(f"Processed CSV not found at {csv_path}")

            vector_build = VectorStoreBuilder(
                csv_path=csv_path,
                persist_directory=persist_dir
            )

            vector_store = vector_build.load_vector_store()
            retriever = vector_store.as_retriever()

            self.recommender = AnimeRecommender(
                retriever=retriever, 
                api_key=GROQ_API_KEY, 
                model_name=MODEL_NAME
            )

            logger.info("Recommendation Pipeline Initialized Successfully...")

        except Exception as e:
            logger.error(f"Error initializing pipeline: {str(e)}")
            raise CustomException("Failed to initialize recommendation pipeline") from e

    def recommend(self, user_query: str) -> str:
        try:
            logger.info(f"Generating recommendations for query: {user_query}")
            recommendation = self.recommender.get_recommendation(user_query)
            logger.info("Recommendation generated successfully...")
            return recommendation

        except Exception as e:
            logger.error(f"Error during recommendation: {str(e)}")
            raise CustomException("Failed to generate recommendations") from e