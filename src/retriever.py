# retriever.py


from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from config import VECTOR_DB_DIR, EMBEDDING_MODEL, TOP_K, OPENAI_API_KEY, BASE_URL


def get_retriever():
    embeddings = OpenAIEmbeddings(
        api_key = OPENAI_API_KEY,
        base_url = BASE_URL,
        model=EMBEDDING_MODEL)

    vectordb = Chroma(
        embedding_function=embeddings,
        persist_directory=VECTOR_DB_DIR,
        collection_metadata = {'hnsw:space': 'cosine'},
        collection_name = 'powerBI_collection',
       
    )

    retriever = vectordb.as_retriever(
        search_type="similarity",
        search_kwargs={"k": TOP_K}
    )

    return retriever

if __name__ == "__main__":
    user_query = 'How to access the power query editor in Power BI?'
    retrieve = get_retriever()
    results = retrieve.invoke(user_query)
    for i, doc in enumerate(results, 1):
        print(f'Document {i} \n{doc.page_content} \n')
