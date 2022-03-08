import streamlit as st
import pandas as pd

st.title('Translate the Law')
st.write('#')
st.subheader('Search for a case by keyword')
st.caption("Need to quickly understand a UK Supreme Court case?\
    Search the one you're looking for by name, justice, case ID, or other keyword.")

case_search = st.text_input(
    'Search for case by keyword')
#not sure how to make text in search bar lighter but something to consider

menu = st.sidebar.title('Menu')
options = st.sidebar.radio('Choose a case', ('Select case from year',
                               'Search case by keyword',
                               'Upload your own text'))
