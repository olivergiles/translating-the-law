import streamlit as st
import pandas as pd

questions_df = pd.DataFrame({'questions': ['Sample Question 1', 'Sample Question 2']})

st.header("Bloomberg LP (Appellant) v ZXC (Respondent)")
st.subheader("Summary")

c = st.container()
c.write("The model generated summary will show up here,\
        along with some of the other relevant case details such as case id number,\
            judgment date, names of justices, and neutral citation number(?)")

st.subheader("Ask a question")

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
