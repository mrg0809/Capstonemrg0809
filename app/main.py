from dotenv import load_dotenv
import chainlit as cl
import openai
import os
from langchain import PromptTemplate, OpenAI, LLMChain, ConversationChain
from langchain.memory import ConversationBufferWindowMemory

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY

template = """Esta conversación es entre el asistente virtual de Operadora Fan del Noroeste y un colaborador
Current convesation: {history}
Question: {question}
Answer: Let's think step by step"""

@cl.on_chat_start
def main():
    prompt = PromptTemplate(template = template, input_variables = ["history", "question"])
    llm_chain = LLMChain(
        prompt = prompt,
        llm = OpenAI(temperature=0, streaming=True),
        verbose = True,
        memory= ConversationBufferWindowMemory(k=2),
    )

    cl.user_session.set("llm_chain", llm_chain,)

@cl.on_message
async def main(message : str):
    llm_chain = cl.user_session.get("llm_chain")

    res = await llm_chain.acall(message, callbacks=[cl.AsyncLangchainCallbackHandler()])

    await cl.Message(content=res["text"]).send()