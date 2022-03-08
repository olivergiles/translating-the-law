import streamlit as st
import pandas as pd
import requests

def app():
    st.title('Translate the Law')
    st.write('#')
    st.subheader('Upload your own case')
    st.caption("Have a court judgment or press release you want to understand?\
        Enter the text of your document below to have it quickly summarized.")
    txt = st.text_area('Enter judgment text for summarization',
                       max_chars=None,
                       placeholder='Max char: ?')
    summary = requests.get(f'https://uskc-summarizer-app-jaefennyiq-ew.a.run.app/summary?text={txt}').json()['summary']
    st.write('The text you entered was:', summary)
    st.write("The model-generated summary will show up here")

    #st.sidebar.title('Choose a case:')
    #st.sidebar.button('Select case from year')
    #st.sidebar.button('Search case by keyword')
    #st.sidebar.button('Upload your own text')


    #if or def to stop summary from running before text is defined
    #run it via a button instead of just through the box for clearer results
    #sometimes after we've been using the site too much, the multiapp nav gets weird
    #(aka stops working)
