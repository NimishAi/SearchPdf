import streamlit as st
from Retrieval import retrieve_and_respond

st.title('Query Uploaded PDF')

with st.form(key='my_form'):
    user_input = st.text_input('Enter your text:')
    submit_button = st.form_submit_button(label='Submit')

    if submit_button:
        response = retrieve_and_respond(user_input)
        st.text_area('Response:', value=response, height=150)