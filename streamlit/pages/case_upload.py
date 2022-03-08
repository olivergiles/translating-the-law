import streamlit as st
import pandas as pd

def app():
    st.title('Translate the Law')
    st.write('#')
    st.subheader('Upload your own case')
    st.caption("Have a court judgment or press release you want to understand?\
        Enter the text of your document below to have it quickly summarized.")
    txt = st.text_area('Enter judgment text for summarization',
                       max_chars=None,
                       placeholder='Max char: ?')
    st.write('The text you entered was:', txt)
    st.write("The model-generated summary will show up here")

    #st.sidebar.title('Choose a case:')
    #st.sidebar.button('Select case from year')
    #st.sidebar.button('Search case by keyword')
    #st.sidebar.button('Upload your own text')
