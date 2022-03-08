import streamlit as st
import pandas as pd

questions_df = pd.DataFrame({'questions': ['Sample Question 1', 'Sample Question 2']})

st.header("Bloomberg LP (Appellant) v ZXC (Respondent)")
st.subheader("Summary")

s = st.container()
s.write("The model-generated summary will show up here,\
        along with some of the other relevant case details such as case id number,\
            judgment date, names of justices, and neutral citation number(?)")

st.subheader("Q&A")

col1, col2 = st.columns(2)
with col1:
    years_option = st.selectbox(
        'Suggested questions',
        questions_df['questions']
        )
with col2:
    case_search = st.text_input(
        'Or write your own',
        'Ask a question about this case')

a = st.container()
a.write("The model-generated answer(s) will show up here")


menu = st.sidebar.title('Menu')

options = st.sidebar.radio('Choose a new case', ('Select case from year',
                               'Search case by keyword',
                               'Upload your own judgment text for summarization'))
