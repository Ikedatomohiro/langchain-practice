from dotenv import load_dotenv
from langchain_community.document_loaders import UnstructuredFileLoader
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import CharacterTextSplitter
from langchain_chroma import Chroma



load_dotenv()
# files = ["./example_data/whatsapp_chat.txt", "./example_data/layout-parser-paper.pdf"]

raw_documents = UnstructuredFileLoader('sample.pdf').load()

print(raw_documents.page_content[:400])

# text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
# documents = text_splitter.split_documents(raw_documents)

# db = Chroma.from_documents(documents, OpenAIEmbeddings())

# query = "What did the president say about Ketanji Brown Jackson"
# docs = db.similarity_search(query)
# print(docs[0].page_content)

# embedding_vector = OpenAIEmbeddings().embed_query(query)
# docs = db.similarity_search_by_vector(embedding_vector)
# print(docs[0].page_content)
