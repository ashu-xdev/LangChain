from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_anthropic import ChatAnthropic
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage


load_dotenv()

llm = ChatOpenAI(model="gpt-4o")

messages = [
    SystemMessage("Solve he following Math problem"),
    HumanMessage("What is the square root of 49?")
]

result = llm.invoke(messages)
print(result.content)


#this is incomplete and might require other models to incoprate into it