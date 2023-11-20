import pandas as pd
import numpy as np
import streamlit as st

def data_col(df):
    if 'cached_column' not in st.session_state:
        cat_col=[]
        num_col=[]
        for i in df.columns:
            if df[i].dtype == 'object':
                cat_col.append(i)
            else:
                num_col.append(i)
            
        st.session_state.cached_data_col = {
            "categorical_columns": list(set(cat_col)),
            "numerical_columns": list(set(num_col))
        }

    return st.session_state.cached_data_col["categorical_columns"], st.session_state.cached_data_col["numerical_columns"]


def summarize_columns(df):
    # Create an empty DataFrame to store the summary
    summary_df = pd.DataFrame(columns=['Column', 'Value Counts', 'Unique Values', 'Missing Values'])

    for column in df.columns:
        value_counts = df[column].value_counts().sum()
        unique_values = len(df[column].unique())
        missing_values = df[column].isnull().sum()

        summary_df = summary_df.append({
                'Column': column,
                'Value Counts': value_counts,
                'Unique Values': unique_values,
                'Missing Values': missing_values
        }, ignore_index=True)

    return summary_df

