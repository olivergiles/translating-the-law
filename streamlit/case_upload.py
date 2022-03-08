import streamlit as st
import pandas as pd

st.title('Translate the Law')
#st.header('Translate the Law')
st.subheader('Upload your own case')
st.caption("Have a court judgment or press release you want to understand?\
    Enter the text of your document below to have it quickly summarized.")

upload_case = st.text_area('Enter judgment text for summarization')

menu = st.sidebar.title('Menu')

options = st.sidebar.radio('Choose a case', ('Select case from year',
                               'Search case by keyword',
                               'Upload your own judgment text for summarization'))
