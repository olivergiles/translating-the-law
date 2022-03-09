import streamlit as st
import pandas as pd

questions_df = pd.DataFrame({'questions': ['Please select', 'Sample Question 1', 'Sample Question 2']})

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
    if st.button('casenameplaceholder'):
        st.write('#')
        st.header('casenameplaceholder')
        st.write('##')
        st.subheader("Summary")
        st.write("The model-generated summary will show up here,\
            along with some of the other relevant case details such as case id number,\
            judgment date, names of justices, and neutral citation number(?)")
        st.write('##')
        st.subheader('Q&A')
        col1, col2 = st.columns([2,3])
        with col1:
            our_q = st.selectbox('Suggested questions', questions_df['questions'])
        with col2:
            new_q = st.text_input('Or write your own', placeholder='Ask a question about this case')
        if our_q != 'Please select':
            st.write(f'Q: {our_q}')
        else:
            st.write(f'Q: {new_q}')
        st.write("A: The model-generated answer(s) will show up here")
