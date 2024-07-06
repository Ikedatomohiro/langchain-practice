import os
from dotenv import load_dotenv
from langchain_openai import OpenAI

load_dotenv()

llm = OpenAI(temperature=0)

result = llm.invoke("自己紹介してください")
print(result.strip())
