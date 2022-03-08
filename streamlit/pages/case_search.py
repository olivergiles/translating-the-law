import streamlit as st
import pandas as pd

def app():
    st.title('Translate the Law')
    st.write('#')
    st.subheader('Search for a case by keyword')
    st.caption("Need to quickly understand a UK Supreme Court case?\
        Search the one you're looking for by name, justice, case ID, or other keyword.")
    query = st.text_input('Search for case by keyword',
                  placeholder='Enter case detail or topic')
    st.write('Search results for: ', query)

    #st.sidebar.title('Choose a case:')
    #st.sidebar.button('Select case from year')
    #st.sidebar.button('Search case by keyword')
    #st.sidebar.button('Upload your own text')
