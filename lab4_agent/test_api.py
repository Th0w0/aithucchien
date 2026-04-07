import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI


load_dotenv()

# llm = ChatOpenAI(
#     model="gpt-4o-mini",
#     temperature=0,
#     openai_api_key=os.getenv("OPENAI_API_KEY")
# )
# print(llm.invoke("What is the capital of France?").content)
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0,
    google_api_key=os.getenv("GOOGLE_API_KEY"),
)

response = llm.invoke("What is the capital of France?")
print(response.content)