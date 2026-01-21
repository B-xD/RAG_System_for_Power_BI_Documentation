# ingest.py

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from config import PDF_PATH, CHUNK_SIZE, CHUNK_OVERLAP, ENCODING_NAME

#Load our pdf file from the data directory 
loader = PyPDFLoader(PDF_PATH)
documents = loader.load()

def doc_splitter(documents, chunk_size, chunk_overlap):
    """ split the document into chunks   """
    
    splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
        encoding_name = ENCODING_NAME,
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP
    )

    chunks = splitter.split_documents(documents)

    if chunks:
        for i, chunk in enumerate(chunks):
            print(f'\n --- chunk {i+1} --')
            print(f'producer:{chunk.metadata['producer']}')
            print(f'creator:{chunk.metadata['creator']}')
            print(f'creationdate:{chunk.metadata['creationdate']}')
            print(f'author:{chunk.metadata['author']}')
            print(f'title:{chunk.metadata['title']}')
            print(f'Source:{chunk.metadata['source']}')
            print(f'total_pages:{chunk.metadata['total_pages']}')
            print(f'page:{chunk.metadata['page']}')
            print(f'page_label:{chunk.metadata['page_label']}')
            print(f'Length: {len(chunk.page_content)} characters')
            print(f'content:')
            print(chunk.page_content)
            print('-'*40)

    return chunks


if __name__ == "__main__":
    chunks = doc_splitter(documents,CHUNK_SIZE, CHUNK_OVERLAP )
    print(f"Loaded {len(chunks)} chunks from PDF")
