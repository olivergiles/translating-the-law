import streamlit as st
from multiapp import MultiApp
from pages import case_search, case_upload, year_select

app = MultiApp()

app.add_app('Select case from year', year_select.app)
app.add_app('Search case by keyword', case_search.app)
app.add_app('Upload your own text', case_upload.app)

app.run()
