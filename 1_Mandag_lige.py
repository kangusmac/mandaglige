import streamlit as st
import pandas as pd
import numpy as np

@st.cache_data
def load_data():

    df = pd.read_csv('data/mandag_lige_merged.csv')
    return df



df = load_data()

df_beholdere = df.groupby(['gade', 'beholder']).agg({'beholder': 'count'}).rename(columns={'beholder': 'antal'}).reset_index()

st.write('## Mandag lige')
st.write('### Tømninger:')

st.dataframe(df_beholdere, use_container_width=False)

