import streamlit as st
from multiapp import MultiApp
from pages import case_search, case_upload, year_select, case_result

app = MultiApp()

app.add_app('Select case from year', year_select.app)
app.add_app('Search case by keyword', case_search.app)
app.add_app('Upload your own text', case_upload.app)

#we will probably have to figure out how to hide this from the nav options
app.add_app('Case summary', case_result.app)


app.run()
