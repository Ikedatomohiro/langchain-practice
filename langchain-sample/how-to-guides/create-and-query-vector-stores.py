from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import CharacterTextSplitter
from langchain_chroma import Chroma

load_dotenv()

# テキストファイルの読み込み
raw_documents = TextLoader('sample.txt').load()

# テキストを小さなチャンクに分割
text_splitter = CharacterTextSplitter(chunk_size=100, chunk_overlap=20)
documents = text_splitter.split_documents(raw_documents)

# インデックスの作成
db = Chroma.from_documents(documents, OpenAIEmbeddings())
print(db)

# クエリの設定
query = "間伐材を使用したコピー用紙の購入量はどのくらいですか？"
embedding_vector = OpenAIEmbeddings().embed_query(query)

# 検索結果の取得
docs = db.similarity_search_by_vector(embedding_vector)

# 検索結果の表示
for i, doc in enumerate(docs):
    print(f"Result {i}:")
    print(doc.page_content)
