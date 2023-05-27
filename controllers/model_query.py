from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.agents import load_tools
from langchain.agents import initialize_agent
import os


from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)

class ModelQueryController:
    def __init__(self):
        self.llm = ChatOpenAI(
            model="gpt-3.5-turbo-0301",
            openai_api_key=os.getenv("OPENAI_API_KEY")
            )
        
    def generic_query(self, prompt):
        messages = [
            SystemMessage(content="You are a helpful assistant"),
            HumanMessage(content="Hi AI, how are you today?"),
            AIMessage(content="I'm great thank you. How can I help you?"),
            HumanMessage(content=prompt)
        ]

        return self.query(messages)
    
    def market_research_query(self, companies):
         messages = [
            SystemMessage(content="You are a helpful assistant"),
            HumanMessage(content="Hi AI, how are you today?"),
            AIMessage(content="I'm great thank you. How can I help you?"),
            HumanMessage(
            content="Generate a brief report on the products,"
             f"strategies, and market perception the following: {' '.join(companies)}")
        ]
         
         return self.query(messages)
    
    def social_media_post(self, prompt):
        messages = [
            SystemMessage(content="You are a helpful assistant"),
            HumanMessage(content="Hi AI, how are you today?"),
            AIMessage(content="I'm great thank you. How can I help you?"),
           HumanMessage(
            content=f"Generate a brief social media marketing post given the following description: {prompt}")
        ]

        return self.query(messages)
        
    def query(self, messages):
        result = self.llm(messages)
        return result.content