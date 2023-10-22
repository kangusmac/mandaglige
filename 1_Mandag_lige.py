import streamlit as st
import pandas as pd
import numpy as np



@st.cache_data
def load_data():

     df = pd.read_csv('data/mandag_ulige_merged.csv')
     df['nr'] = df['gade'].str.extract('(\d+)').astype(int)
     df['gade'] = df['gade'].str.extract('(\D+)')

     return df



df = load_data()
#df.sort_values(by=['gade', 'beholder'], inplace=True)
df_gb = df.sort_values(by = ['gade', 'nr', 'beholder'], ascending = True).groupby(['gade', 'nr', 'beholder'])['antal'].sum().reset_index()


#df_beholdere = df.groupby(['gade', 'beholder', ]).agg({'beholder': 'count'}).rename(columns={'beholder': 'antal'}).reset_index()
df_gb = df.groupby(['gade','nr', 'beholder'])['antal'].sum()
#df_beholdere.sort_values(by=['gade', 'beholder'], inplace=True)

st.write('## Mandag ulige')
st.write('### Tømninger:')


#'''color every second row'''
def highlight_second(x):
    df = x.copy()
    df.loc[::2] = 'background-color: #f2f2f2'
    return df


st.dataframe(df_gb, use_container_width=True)

