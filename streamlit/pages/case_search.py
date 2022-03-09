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
    if st.button('Enter'):
        st.write('Search results for: ', query)
    else:
        pass
