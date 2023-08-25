import streamlit as st
from compare_llm_handler import compare_clauses
from suggestion_llm_handler import suggest_amendments

# Client code below

st.set_page_config(page_title="Davide", page_icon=":writing_hand:")
st.header("Davide")
st.text("A legal AI toolkit")

option_choice = st.selectbox(
   "What do you need help with?",
   ('Compare', 'Suggest Amendments', 'Summarize')
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

if option_choice == 'Suggest Amendments':
   clauseText = st.text_area(label="Clause", height=200, placeholder="Add clause here", key="clause")
   favorableParty = st.text_area(label="Favorable Party", height=50, placeholder="Indicate which party you'd prefer to suggest favorable amendments to", key="favorable_party")
   
   if st.button('Submit'):
      with st.spinner("Finding amendment suggestions..."):
          suggested_amendments = suggest_amendments(clauseText, favorableParty)
          suggested_amendments
          
elif option_choice == 'Summarize':
   "Summarize is not yet supported"

