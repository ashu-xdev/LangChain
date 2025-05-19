from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

load_dotenv()

llm = ChatOpenAI(model="gpt-4o")

chat_history = [] # use a list to store the chat history

#Set intial system message (Optionsla)
system_message = SystemMessage("You are a helpful AI assistant")
chat_history.append(system_message) # Add system message to chat history

while True:
    query = input("You: ")
    if(query.lower() == "exit"):
        break;
    chat_history.append(HumanMessage(content=query))

    #Get AI response using history
    result = llm.invoke(chat_history)
    response  = result.content
    chat_history.append(AIMessage(content=response))
    
    print(f"AI: {response}")

print("---- Message History ----")
print(chat_history)