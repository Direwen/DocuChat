from langchain_text_splitters import SpacyTextSplitter
from dotenv import load_dotenv
import os

load_dotenv()

DEFAULT_CHUNK_SIZE = int(os.environ.get("CHUNK_SIZE", 1500))
DEFAULT_CHUNK_OVERLAP = int(os.environ.get("CHUNK_OVERLAP", 150))

# Initialize the splitter
def get_text_splitter(chunk_size: int = DEFAULT_CHUNK_SIZE, chunk_overlap: int = DEFAULT_CHUNK_OVERLAP):
    return SpacyTextSplitter(
        chunk_size=chunk_size, 
        chunk_overlap=chunk_overlap
    )