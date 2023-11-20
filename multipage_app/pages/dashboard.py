import random
import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px 
import plotly.graph_objects as go
from Pipeline.data_visualizer import plot_metric, plot_gauge, plot_bottom_left, plot_bottom_right, plot_top_right
from Pipeline.formula import revenue, cogs

st.set_page_config(
    page_title = "Descriptive Analysis",
    page_icon = "🎢",
    layout = "wide"
)

df = st.session_state.uploaded_data

years  = list(df.Year.unique())
scenario = list(df.Scenario.unique())


col1, col2 = st.columns(2)
with col1:
    years_selected = st.multiselect('Year', years )
with col2:
    scenario_selected = st.multiselect('Scenario', scenario)

rev = revenue(df, years_selected, scenario_selected)

cog = cogs(df, years_selected)

top_left_column, top_right_column = st.columns((2, 1))
bottom_left_column, bottom_right_column = st.columns(2)

with top_left_column:
    column_1, column_2, column_3, column_4 = st.columns(4)

    with column_1:
        plot_metric(
            "Total Accounts Receivable",
            revenue(df, years_selected, scenario_selected),
            prefix="$",
            suffix="",
            show_graph=True,
            color_graph="rgba(0, 104, 201, 0.2)",
        )
        plot_gauge(1.86, "#0068C9", "%", "Current Ratio", 3)

    with column_2:
        plot_metric(
            "Total Accounts Payable",
            cogs(df, years_selected),
            prefix="$",
            suffix="",
            show_graph=True,
            color_graph="rgba(255, 43, 43, 0.2)",
        )
        plot_gauge(10, "#FF8700", " days", "In Stock", 31)

    with column_3:
        plot_metric("Equity Ratio", 75.38, prefix="", suffix=" %", show_graph=False)
        plot_gauge(7, "#FF2B2B", " days", "Out Stock", 31)
        
    with column_4:
        plot_metric("Debt Equity", 1.10, prefix="", suffix=" %", show_graph=False)
        plot_gauge(28, "#29B09D", " days", "Delay", 31)

with top_right_column:
    plot_top_right()

with bottom_left_column:
    plot_bottom_left()

with bottom_right_column:
    plot_bottom_right()
