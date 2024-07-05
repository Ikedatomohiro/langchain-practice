from langchain_openai import OpenAI

llm = OpenAI(temperature=0)

result = llm.invoke("自己紹介してください")
print(result.strip())
