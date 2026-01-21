# Power BI RAG Documentation Assistant

powerbi-rag-documentation-assistant/
├── data/
│   └── PowerBI.pdf
├── vector_db/
│   └── powerBI_db/
├── src/
│   ├── ingest.py          # PDF loading + chunking
│   ├── embeddings.py     # Vector DB creation
│   ├── retriever.py      # Similarity search
│   ├── prompts.py        # System & user prompts
│   ├── rag_chat.py       # CLI chatbot
│   └── config.py
├── notebooks/
│   └── exploration.ipynb
├── requirements.txt
├── README.md
└── .gitignore


## Overview
A Retrieval-Augmented Generation (RAG) system that enables users to query
official Microsoft Power BI documentation using natural language and receive
accurate, citation-grounded answers.

## Business Problem
Business Context: Power BI Knowledge Accessibility Challenge
Power BI is one of the most widely used business intelligence platforms for data analysis and reporting. Despite its power, analysts often struggle to fully utilize its capabilities due to the size, complexity, and fragmentation of official documentation. Important concepts such as Power Query, DAX functions, data modeling, and report design are scattered across hundreds of pages, making it difficult to quickly locate precise answers.
As a result:
* Analysts waste time searching documentation
* Features are misunderstood or underutilized
* Decision-making is delayed
* Business value from Power BI investments is reduced

Solution: Retrieval-Augmented Generation (RAG) System for Power BI
This project implements a Retrieval-Augmented Generation (RAG) system that allows analysts to query official Power BI documentation using natural language and receive accurate, citation-grounded answers in real time.
The system:
* Indexes official Power BI PDF documentation
* Retrieves the most relevant content using vector similarity search
* Generates responses using a large language model strictly grounded in retrieved documents
* Provides page-level citations for every answer
This approach significantly improves documentation accessibility, reduces onboarding time, and enables analysts to make faster, more informed decisions.

## Solution Architecture
- PDF ingestion & chunking
- OpenAI embeddings
- ChromaDB vector storage
- Similarity-based retrieval
- GPT-based answer generation with citations

## RAG Pipeline
| Stage | Description |
|------|------------|
| Indexing | Chunking, embedding, vector storage |
| Retrieval | Semantic similarity search |
| Generation | LLM response grounded in retrieved context |

## Technologies Used
- OpenAI (GPT-4o-mini, text-embedding-3-small)
- LangChain
- ChromaDB
- Python
- Google Colab
- VS Code 

## How to Run
```bash
python src/rag_chat.py

