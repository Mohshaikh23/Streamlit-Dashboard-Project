import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px 

st.set_page_config(
    page_title = "Descriptive Analysis",
    page_icon = "🎢",
    layout = "wide"
)

df = st.session_state.uploaded_data

categorical_columns, numerical_columns = st.session_state.cat_num

new_df = df.drop(['Year'], axis = 1)

# st.button('Click here')
# temp = 0
# for i in new_df[categorical_columns]:
#     temp = new_df.groupby(by=i).sum()
#     st.write(i)
#     st.plotly_chart(px.bar(data_frame=temp,  x = temp.index, y=temp.columns ))

if st.session_state is not None:
    
    data = df.groupby(by=['Year']).sum() #reset_index()
    Month = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
    Year = data.index.to_list()

    col1, col2 = st.columns(2)
    with col1:
        # Allow user to select multiple Years
        multiselect1 = st.multiselect("Select Year(s)", Year)

    with col2:
        # Allow user to select multiple Months
        multiselect2 = st.multiselect("Select Month(s)", Month)
    
    filtered_data = data.loc[multiselect1, multiselect2]
    
    if filtered_data.empty:
        filtered_data = data
        st.info("Please select Names and Months to customize the charts.")
    
    col1 , col2 = st.columns((2, 1))

    with col1:
        st.plotly_chart(px.line(data_frame=filtered_data, 
            x =filtered_data.index,
            y=filtered_data.columns ).update_layout(width=1000))

    with col2:
        st.plotly_chart(px.pie(data_frame=filtered_data, 
            names=filtered_data.index, 
            values=filtered_data.sum(axis=1)).update_layout(width=500))


    st.plotly_chart(px.imshow(filtered_data, 
                              text_auto=True, 
                              aspect="auto").update_layout(width=1000))
