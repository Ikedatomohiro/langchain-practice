from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
import requests
from bs4 import BeautifulSoup
from langchain import hub
from langchain_chroma import Chroma# from langchain_community.document_loaders import WebBaseLoader
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import OpenAIEmbeddings
from langchain_core.documents import Document
import html
from langchain_text_splitters import RecursiveCharacterTextSplitter

load_dotenv()
llm = ChatOpenAI(model="gpt-3.5-turbo-0125")

# WebBaseLoaderの代わりに手動でHTMLを取得してエンコーディングを設定
url = "https://zenn.dev/cykinso/articles/e1566fd95641c3/"
response = requests.get(url)
response.encoding = response.apparent_encoding  # エンコーディングを自動的に推測して設定

soup = BeautifulSoup(response.content, 'html.parser')

# 具体的なクラス名でフィルタリング
content = ""
target_tags = soup.find_all()
for tag in target_tags:
    text = html.unescape(tag.get_text(separator="\n").strip())
    content += text + "\n"

# ドキュメントオブジェクトに変換
docs = [Document(page_content=content, metadata={"source": url})]

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
splits = text_splitter.split_documents(docs)

print(len(splits))
vectorstore = Chroma.from_documents(documents=splits, embedding=OpenAIEmbeddings())

# Retrieve and generate using the relevant snippets of the blog.
retriever = vectorstore.as_retriever()
prompt = hub.pull("rlm/rag-prompt")


def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)


rag_chain = (
    {"context": retriever | format_docs, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)

res = rag_chain.invoke("記事に利用されているPythonのバージョンを示してください")

print(res)
