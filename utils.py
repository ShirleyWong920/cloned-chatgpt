"""
author:ws
"""
from langchain.memory import ConversationBufferMemory,ConversationSummaryMemory
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate,MessagesPlaceholder
from langchain.chains import ConversationChain

def createChain(api_key, model= 'gpt-3.5-turbo') -> ConversationChain:
    model = ChatOpenAI(model = model, openai_api_key = api_key,
                      openai_api_base = 'https://api.aigc369.com/v1')

    memory = ConversationSummaryMemory(return_messages = True, llm = model)

    chain = ConversationChain(llm = model, memory = memory)

    return chain

def getAIMessage(input, chain) -> str :
    response = chain.invoke({"input": input})
    print(response)
    return response["response"]

