# embeddings.py

from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
from ingest import load_and_chunk_pdf
from config import VECTOR_DB_DIR, EMBEDDING_MODEL


def create_vector_db():
    documents = load_and_chunk_pdf()

    embeddings = OpenAIEmbeddings(model=EMBEDDING_MODEL)

    vectordb = Chroma.from_documents(
        documents=documents,
        embedding=embeddings,
        persist_directory=VECTOR_DB_DIR
    )

    vectordb.persist()
    return vectordb


if __name__ == "__main__":
    db = create_vector_db()
    print("Vector database created and saved.")
