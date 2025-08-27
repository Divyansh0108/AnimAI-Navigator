from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain_community.embeddings import SentenceTransformerEmbeddings
from utils.logger import get_logger
import os

from dotenv import load_dotenv

load_dotenv()

logger = get_logger()


class VectorStoreBuilder:
    def __init__(self, csv_path: str, persist_directory: str = "chroma_db"):
        self.csv_path = csv_path
        self.persist_dir = persist_directory

        os.environ.pop("HF_TOKEN", None)
        os.environ.pop("HUGGINGFACEHUB_API_TOKEN", None)

        try:
            self.embeddings = SentenceTransformerEmbeddings(
                model_name="all-MiniLM-L6-v2"
            )
            logger.info("Successfully loaded embeddings")
        except Exception as e:
            logger.error(f"Failed to load embeddings: {e}")
            try:
                from langchain_huggingface import HuggingFaceEmbeddings

                self.embeddings = HuggingFaceEmbeddings(
                    model_name="all-MiniLM-L6-v2", model_kwargs={"device": "cpu"}
                )
                logger.info("Successfully loaded HuggingFace embeddings as fallback")
            except Exception as e2:
                logger.error(f"Both embedding methods failed: {e2}")
                raise

    def build_and_save_vectorstore(self):
        loader = CSVLoader(
            file_path=self.csv_path, encoding="utf-8", metadata_columns=[]
        )
        data = loader.load()
        splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
        text = splitter.split_documents(data)

        db = Chroma.from_documents(
            documents=text,
            embedding=self.embeddings,
            persist_directory=self.persist_dir,
        )
        db.persist()

    def load_vector_store(self):
        return Chroma(
            embedding_function=self.embeddings, persist_directory=self.persist_dir
        )
