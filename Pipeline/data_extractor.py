import streamlit as st
import pandas as pd
from pathlib import Path

@st.cache_data
def load_data(path:str):
    data = pd.read_excel(path)
    return data

def dataframe_(uploaded_file):
    file_extension = uploaded_file.name.split('.')[-1]
    if file_extension.lower() == 'csv':
        df = pd.read_csv(uploaded_file)
    elif file_extension.lower() in ['xlsx', 'xls']:
        df = pd.read_excel(uploaded_file)
    else:
        st.error("Unsupported file format. Please upload a CSV, XLSX, or XLS file.")
        st.stop()

    return df