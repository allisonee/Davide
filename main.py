import streamlit as st
import os
from langchain import PromptTemplate
from langchain.llms import OpenAI

# LLM code below

template = """
  Compare the following two clauses and identify any inconsistencies between them. Do not identify inconsistencies that are immaterial or insubstantial (for example, ignore inconsistencies in language and style). Only identify material inconsistencies that alter the meaning of the text, including any differences in scope between the two clauses.

  Below are the two clauses:
  FIRST_CLAUSE: {first_clause}
  SECOND_CLAUSE: {second_clause}

  YOUR RESPONSE:
"""

prompt = PromptTemplate(
  input_variables=("first_clause", "second_clause"),
  template=template,
)

def load_LLM():
  llm = OpenAI(temperature=0, model_name="gpt-4")
  return llm

llm = load_LLM()


# Client code below

st.set_page_config(page_title="Davide", page_icon=":writing_hand:")
st.header("Davide")
st.text("A legal AI toolkit")

option_choice = st.selectbox(
   "What do you need help with?",
   ('Compare', 'Summarize')
)

if option_choice == 'Compare':
  col1, col2 = st.columns(2)
  
  with col1:
    textFirstClause = st.text_area(label="First clause", height=300, placeholder="Add first clause here", key="clause_1")

  with col2:
    textSecondClause = st.text_area(label="Second clause", height=300, placeholder="Add second clause here", key="clause_2")

  if st.button('Submit'):
      with st.spinner("Comparing the clauses..."):
          prompt_with_clauses = prompt.format(first_clause=textFirstClause, second_clause=textSecondClause)
          compared_clauses = llm(prompt_with_clauses)
          
          st.write(compared_clauses)

elif option_choice == 'Summarize':
   "Summarize is not yet supported"

