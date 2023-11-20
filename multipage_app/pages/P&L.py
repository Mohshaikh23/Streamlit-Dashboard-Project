import streamlit as st
import pandas as pd

# Assume df is your DataFrame
# Create a Streamlit app
st.title("Profit and Loss Statement")

df = st.session_state.uploaded_data

col1, col2 = st.columns(2)

with col1:
    # Select unique years and scenarios
    years = df['Year'].unique()
    selected_year = st.selectbox("Select Year", years)
with col2:
    scenarios = df['Scenario'].unique()
    selected_scenario = st.selectbox("Select Scenario", scenarios)

# Filter DataFrame based on user selection
filtered_df = df[(df['Year'] == selected_year) & (df['Scenario'] == selected_scenario)]


# Filter DataFrame based on user selection
filtered_df = df[(df['Year'] == selected_year) & (df['Scenario'] == selected_scenario)]

# Define categories
categories = ['Sales', 'Cost of Goods Sold', 'Gross Profit','Commissions Expense', 'Payroll Expense',
              'Travel & Entertainment Expense', 'R&D Expense', 'Consulting Expense',
              'Software/Hardware Expense', 'Marketing Expense']

# Create a DataFrame with summarized data
pl_df = pd.DataFrame(index=categories, columns=['Amount'])

all_months =['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
# Fill in data for each category
pl_df.loc['Sales'] = filtered_df.loc[filtered_df['Account'] == 'Sales',
                                     all_months ].sum().sum()
pl_df.loc['Cost of Goods Sold'] = filtered_df.loc[filtered_df['Account'] == 'Cost of Goods Sold',
                                                  all_months].sum().sum()
pl_df.loc['Gross Profit'] = pl_df.loc['Sales'] - abs(pl_df.loc['Cost of Goods Sold'])
pl_df.loc['Commissions Expense'] = filtered_df.loc[filtered_df['Account'] == 'Commissions Expense', 
                                                   all_months].sum().sum()
pl_df.loc['Payroll Expense'] = filtered_df.loc[filtered_df['Account'] == 'Payroll Expense',
                                               all_months].sum().sum()
pl_df.loc['Travel & Entertainment Expense'] = filtered_df.loc[filtered_df['Account'] == 'Travel & Entertainment Expense',
                                                              all_months].sum().sum()
pl_df.loc['R&D Expense'] = filtered_df.loc[filtered_df['Account'] == 'R&D Expense', all_months].sum().sum()
pl_df.loc['Consulting Expense'] = filtered_df.loc[filtered_df['Account'] == 'Consulting Expense',
                                                  all_months].sum().sum()
pl_df.loc['Software/Hardware Expense'] = filtered_df.loc[filtered_df['Account'] == 'Software/Hardware Expense', 
                                                         all_months].sum().sum()
pl_df.loc['Marketing Expense'] = filtered_df.loc[filtered_df['Account'] == 'Marketing Expense',
                                                 all_months].sum().sum()

# Calculate Total Operating Expenses
pl_df.loc['Total Operating Expenses'] = pl_df.loc[['Commissions Expense', 'Payroll Expense', 'Travel & Entertainment Expense', 'R&D Expense', 'Consulting Expense', 'Software/Hardware Expense', 'Marketing Expense']].sum()

# Calculate Operating Income (Loss)
pl_df.loc['Operating Income (Loss)'] = pl_df.loc['Gross Profit'] - abs(pl_df.loc['Total Operating Expenses'])

index_mapping = [['Revenue','COGS', 'Gross Profit', 'Total Expense', 'Total Expense',
              'Total Expense', 'Total Expense', 'Total Expense',
              'Total Expense', 'Total Expense', 'Total Operating Expenses', 'Operating Income (Loss)'] ,
                 [ 'Sales','Cost of Goods Sold','Gross Profit', 'Commissions Expense', 'Payroll Expense',
              'Travel & Entertainment Expense', 'R&D Expense', 'Consulting Expense',
              'Software/Hardware Expense', 'Marketing Expense', 'Total Operating Expenses', 
                  'Operating Income (Loss)']]

pl_df.index = index_mapping

# pl_df.applymap(lambda x: f'({abs(x):,.2f})' if x < 0 else f'{x:,.2f}')

def format_values(value):
    return f"{'(' if value < 0 else ''}${abs(value):,.2f}{')' if value < 0 else ''}"

# Apply the custom function to format values
formatted_df = pl_df.applymap(format_values)

# Display the formatted DataFrame in Streamlit
st.table(formatted_df)
