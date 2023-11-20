import sys
sys.path.append("E:\END TO END ML PROJECT\Streamlit-Dashboard-Project")  

import streamlit as st
import pandas as pd
from Pipeline.config import get_session_state
from Pipeline.data_extractor import dataframe_
from Pipeline.datamodeller import data_col, summarize_columns


# Get or initialize session state
session_state = get_session_state()

st.set_page_config(
    page_title = "Sales Dashboard",
    page_icon = "🧊",
    layout = "wide"
)

st.title('Sales Dashboard')
col1 , col2 = st.columns(2)
with col1:
    st.markdown('prototype v0.0.1')
with col2:
    if st.session_state is None:
        st.title(session_state)
    # else:
    #     st.title(uploaded_data.name)

with st.sidebar:
    st.header("Configuration")
    
    # Upload file
    uploaded_file = st.sidebar.file_uploader("Choose a file", type=["csv", "xlsx", "xls"])
    
    # Store the uploaded data in session state
    if uploaded_file is not None:
        session_state.uploaded_data = dataframe_(uploaded_file)
    
    # Check if data is uploaded
    if session_state.uploaded_data is None:
        st.info("Upload a file through config", icon="⚒️")
        st.stop()

df = session_state.uploaded_data

select_features = st.multiselect("Select Features", list(df.columns))
if select_features:
        st.dataframe(df[select_features])
        
else:
    with st.expander('Data Preview'):
        st.dataframe(df)
        st.warning("Please select features to display.")



categorical_columns, numerical_columns = data_col(df)

if 'cat_num' is not None:
    session_state.cat_num =  data_col(df)

# Check if data is uploaded
if session_state.cat_num is None:
    st.info("Upload a file through config", icon="⚒️")
    st.stop()

col1, col2 = st.columns(2)

with col1:
    with st.expander("Categorical Columns"):
        cat_df = summarize_columns(df[categorical_columns])
        st.write(cat_df)

with col2:
    with st.expander("Numerical Columns"):
        num_df = summarize_columns(df[numerical_columns])
        st.write(num_df)



