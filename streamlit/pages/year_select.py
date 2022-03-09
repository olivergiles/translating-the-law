from translating_the_law.utils.get_from_bucket import open_from_bucket
import streamlit as st
import pandas as pd

data = open_from_bucket()

case_df = pd.DataFrame([data])
years_df = pd.DataFrame({
    'index': [1, 2, 3, 4, 5, 6, 7, 8, 9 , 10, 11, 12, 13, 14],
    'years': [2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017,
              2018, 2019, 2020, 2021, 2022]
    })

cases_df = pd.DataFrame({
    'index': [1, 2, 3, 4, 5, 6, 7, 8],
    'casename': ["Craig (Appellant) v Her Majesty’s Advocate (for the Government of the United States of America) and another (Respondents) (Scotland)",
                 "Bloomberg LP (Appellant) v ZXC (Respondent)",
                 "Public Prosecutors Office of the Athens Court of Appeal (Appellant) v O'Connor (AP) (Respondent) (Northern Ireland)",
                 "R (on the application of The Project for the Registration of Children as British Citizens) (Appellant) v Secretary of State for the Home Department) (Respondent) (Expedited)",
                 "R (on the application of O (a minor, by her litigation friend AO)) (Appellant) v Secretary of State for the Home Department (Respondent)",
                 "Akdogan and another (AP) (Appellants) v Director of Public Prosecutions (Respondent)",
                 "PWR (AP) (Appellant) v Director of Public Prosecutions (Respondent)",
                 "Firstport Property Services Limited (Appellant) v Settlers Court RTM Company and others (Respondents)"]
    })

questions_df = pd.DataFrame({'questions': ['Please select', 'Sample Question 1', 'Sample Question 2']})


def app():
    st.title('Translate the Law')
    st.write('#')
    st.subheader('Select a case by year')
    st.caption('Need to quickly understand a UK Supreme Court case?\
        Select one from the menu below or choose random to learn something new!')
    col1, col2 = st.columns([1,5])
    with col1:
        st.selectbox('Judgment year',
                     years_df['years'])
    with col2:
        cases_option = st.selectbox('Case name',
                                    cases_df['casename'])
    # st.caption(f'Go to summary: {cases_option}')
    # for bolder text: st.write(f'Go to summary: {cases_option}')
    choose_case = st.button(f'Go to summary: {cases_option}')
    choose_random = st.button('Select a random case')
    if choose_case:
        st.write('#')
        st.header(f'{cases_option}')
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
    elif choose_random:
        #lines for select random case
        st.write('#')
        st.header(f'Placeholder: random case title')
        st.write('##')
        st.subheader("Summary")
        st.write("The model-generated summary will show up here,\
            along with some of the other relevant case details such as case id number,\
            judgment date, names of justices, and neutral citation number(?)")
        st.write('##')
        st.subheader('Q&A')
        col1, col2 = st.columns([2,3])
        with col1:
            our_q = st.selectbox('Suggested questions',
                                questions_df['questions'])
        with col2:
            new_q = st.text_input('Or write your own',
                                placeholder='Ask a question about this case')
        if our_q != 'Please select':
            st.write(f'Q: {our_q}')
        else:
            st.write('Q: ', new_q)
        st.write("A: The model-generated answer(s) will show up here")
    else:
        pass

    #st.sidebar.title('Choose a case:')
    #st.sidebar.button('Select case from year')
    #st.sidebar.button('Search case by keyword')
    #st.sidebar.button('Upload your own text')
