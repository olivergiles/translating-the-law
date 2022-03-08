import streamlit as st
import pandas as pd

#primaryColor = "#B97D60" -- tan
#backgroundColor = "#F0EAD6" -- eggshell
#secondaryBackgroundColor = "#F8FDFD" -- light light robins egg
#textColor = "#04226D" -- navy
#font = "serif"


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
#st.header('Translate the Law')
#st.subheader('Translate the Law')
st.caption('Need to quickly understand a UK Supreme Court case? Select from the menu below or search by keyword to find a concise summary.')

col1, col2 = st.columns(2)

with col1:
    years_option = st.selectbox(
        'What case year?',
        years_df['years'])

with col2:
    cases_option = st.selectbox(
        'Case name',
        cases_df['casename'])

'You selected: ', cases_option
#st.caption(('You selected: ', cases_option))
#can't make the above work; maybe try f string

random_search = st.button('Select a random case')


menu = st.sidebar.title('Custom options')

case_search = st.sidebar.text_input(
    'Search for case by keyword',
    'Case name or Justice')
#not sure how to make text in search bar lighter but something to consider

upload_case = st.sidebar.text_area('Upload your own judgment text for summarization')
