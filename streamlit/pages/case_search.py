import streamlit as st
import pandas as pd

def app():
    st.title('Translate the Law')
    st.write('#')
    st.subheader('Search for a case by keyword')
    st.caption("Need to quickly understand a UK Supreme Court case?\
        Search the one you're looking for by name, justice, case ID, or other keyword.")
    st.text_input('Search for case by keyword')
    #not sure how to make text in search bar lighter but something to consider

    #st.sidebar.title('Choose a case:')
    #st.sidebar.button('Select case from year')
    #st.sidebar.button('Search case by keyword')
    #st.sidebar.button('Upload your own text')
