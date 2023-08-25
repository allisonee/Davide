import streamlit as st
from compare_llm_handler import compare_clauses

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
          compared_clauses = compare_clauses(textSecondClause, textSecondClause)
          compared_clauses
          
elif option_choice == 'Summarize':
   "Summarize is not yet supported"

