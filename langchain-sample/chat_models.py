import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage

load_dotenv()

chat = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.5)

messages = [
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content="こんにちは！私はジョンといいます"),
    AIMessage(content="こんにちはジョンさん！どのようにお手伝いできますか？"),
    HumanMessage(content="私の名前がわかりますか？")
]

result = chat.invoke(messages)
print(result.content)
