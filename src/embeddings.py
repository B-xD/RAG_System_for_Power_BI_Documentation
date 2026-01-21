# embeddings.py

from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
from ingest import doc_splitter
from config import VECTOR_DB_DIR, EMBEDDING_MODEL, OPENAI_API_KEY, BASE_URL


def create_vector_db():
    chunks = doc_splitter()

    embeddings = OpenAIEmbeddings(
        api_key = OPENAI_API_KEY,
        base_url = BASE_URL,
        model=EMBEDDING_MODEL)

    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=VECTOR_DB_DIR,
        collection_metadata = {'hnsw:space': 'cosine'},
        collection_name = 'powerBI_collection'
    )

    #vector_store.persist()
    return vector_store


if __name__ == "__main__":
    db = create_vector_db()
    print("Vector database created and saved.")
