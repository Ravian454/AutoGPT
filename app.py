import os
from apikey import apikey
import streamlit as st
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SimpleSequentialChain



os.environ['OPENAI_API_KEY'] = apikey


# App Layout
st.title('🦜 Search Anything')
prompt = st.text_input("Plug in your prompt here")

#Prompt Templates
title_template = PromptTemplate(
    input_variables = ['topic'],
    template = 'write me a youtube video title about {topic}'
)

script_template = PromptTemplate(
    input_variables = ['title'],
    template = 'write me a youtube video script based on this Title: {topic}'
    
)


#LLms
llm = OpenAI(temperature = 0.9)
title_chain = LLMChain(llm=llm,prompt=title_template ,verbose=True)
if prompt:
    response = title_chain.run(prompt)
    st.write(response)
