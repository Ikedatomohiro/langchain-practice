from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings

load_dotenv()

embeddings_model = OpenAIEmbeddings()

embeddings = embeddings_model.embed_documents(
    [
        "Hi there!",
        "Oh, hello!",
        "What's your name?",
        "My friends call me World",
        "Hello World!"
    ]
)
print(len(embeddings), len(embeddings[0]))

embedded_query = embeddings_model.embed_query("What was the name mentioned in the conversation?")
print(embedded_query[:5])
