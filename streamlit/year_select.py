import streamlit as st
import pandas as pd

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

st.title('Translate the Law')
st.write('#')
st.subheader('Select a case by year')
st.caption('Need to quickly understand a UK Supreme Court case?\
    Select one from the menu below or choose random to learn something new!')

col1, col2 = st.columns([1,5])

with col1:
    years_option = st.selectbox(
        'Judgment year',
        years_df['years'])

with col2:
    cases_option = st.selectbox(
        'Case name',
        cases_df['casename'])

st.caption(f'Go to summary: {cases_option}')
# for bolder text: st.write(f'Go to summary: {cases_option}')

random_search = st.button('Select a random case')

options = st.sidebar.title('Choose a case:')
select_year = st.sidebar.button('Select case from year')
search_keyword = st.sidebar.button('Search case by keyword')
new_case = st.sidebar.button('Upload your own text')

#menu = st.sidebar.title('Menu')
#options = st.sidebar.radio('Choose a case', ('Select case from year',
#                               'Search case by keyword',
#                               'Upload your own judgment text for summarization'))
