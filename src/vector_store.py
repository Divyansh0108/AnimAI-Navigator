from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain_community.embeddings import SentenceTransformerEmbeddings
from utils.logger import get_logger
import os

from dotenv import load_dotenv

load_dotenv()

logger = get_logger()


class VectorStoreBuilder:
    def __init__(self, csv_path: str, persist_directory: str = "faiss_db"):
        self.csv_path = csv_path
        self.persist_dir = persist_directory
        os.makedirs(persist_directory, exist_ok=True)
        self.embeddings = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")

    def build_and_save_vectorstore(self):
        try:
            logger.info("Loading documents from CSV...")
            loader = CSVLoader(file_path=self.csv_path, encoding="utf-8")
            documents = loader.load()

            logger.info("Splitting documents...")
            text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
            texts = text_splitter.split_documents(documents)

            logger.info("Creating FAISS vector store...")
            vectorstore = FAISS.from_documents(texts, self.embeddings)

            logger.info(f"Saving vector store to {self.persist_dir}")
            vectorstore.save_local(self.persist_dir)

            logger.info("Vector store created and saved successfully!")
            return vectorstore

        except Exception as e:
            logger.error(f"Error building vector store: {e}")
            raise

    def load_vector_store(self):
        try:
            logger.info(f"Loading vector store from {self.persist_dir}")
            return FAISS.load_local(
                self.persist_dir, self.embeddings, allow_dangerous_deserialization=True
            )
        except Exception as e:
            logger.error(f"Error loading vector store: {e}")
            raise
