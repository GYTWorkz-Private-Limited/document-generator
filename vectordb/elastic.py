
from langchain_community.document_loaders.pdf import PyPDFLoader
from rag.utils import NLTKSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain_elasticsearch import ElasticsearchStore

embedding = OpenAIEmbeddings()


def index_file(file_path : str, file_type = 'pdf'):
    loader = PyPDFLoader(
        file_path = file_path
    )

    documents = loader.load()
    all_content = ""
    for doc in documents:
        all_content += doc.page_content
    
    chunks = NLTKSplitter().semantic_split(all_content)
    metadata = [ {'file_name' : file_path} for _ in range(len(documents)) ]
    elastic_vector_search = ElasticsearchStore(
        es_url="http://localhost:9200",
        index_name="sections-index",
        embedding=embedding,
        es_user="elastic",
        es_password="changeme"
    )
    elastic_vector_search.add_texts(chunks, metadata)
    # elastic_vector_search.similarity_search_with_score()
    # elastic_vector_search.add


def get_example_from_knowledge(query : str):
    elastic_vector_search = ElasticsearchStore(
        es_url="http://localhost:9200",
        index_name="sections-index",
        embedding=embedding,
        es_user="elastic",
        es_password="changeme"
    )
    docs = elastic_vector_search.similarity_search(query, k = 1)
    return docs[0].page_content

