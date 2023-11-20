import pandas as pd

def revenue(df, year, scenario):
    Revenue = df[(df['Account']=='Sales') 
           & (df['Year'].isin(year)) 
           & (df['Scenario'].isin(scenario))][['Jan','Feb', 'Mar', 'Apr', 'May', 'Jun',
                                    'Jul', 'Aug', 'Sep', 'Oct', 'Nov','Dec']].sum().sum()

    return Revenue

def cogs(df, year):
    cog = df[(df['Account']=='Cost of Goods Sold') 
            & (df['Year'].isin(year))][['Jan','Feb', 'Mar', 'Apr', 'May', 'Jun',
                                    'Jul', 'Aug', 'Sep', 'Oct', 'Nov','Dec']].sum().sum()
    return abs(cog)

