from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from dotenv import load_dotenv

load_dotenv()

from langchain_qdrant import QdrantVectorStore

pdf_path = Path(__file__).parent / "node.pdf"

loader = PyPDFLoader(file_path=pdf_path)
docs = loader.load()

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000, #1000 characters
    chunk_overlap=200, #overlap of 200 characters
)

split_docs = text_splitter.split_documents(documents=docs)

embedder = OpenAIEmbeddings(
    model="text-embedding-3-large",
    api_key=""
)

vector_store = QdrantVectorStore.from_documents(
     documents=[],
     url="http://localhost:6333",
     collection_name="learning_langchain",
     embedding=embedder
 )

vector_store.add_documents(documents=split_docs)

print("Data Injestion Done")