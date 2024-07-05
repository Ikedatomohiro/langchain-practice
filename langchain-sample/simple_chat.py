from langchain_openai import ChatOpenAI

chat = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.5)
result = chat.invoke("hello")

print(result.content)
