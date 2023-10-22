import pandas as pd
import folium
import streamlit as st
from streamlit_folium import st_folium




@st.cache_data
def read_data():
    df = pd.read_csv('data/mandag_ulige_merged.csv')
    return df

def create_map(df):
    lat_avg = df.latitude.mean()
    lng_avg = df.longitude.mean()
    m = folium.Map(location=[lat_avg, lng_avg], zoom_start=17)
    for _, row in df.iterrows():
        folium.Marker(
            [row.latitude, row.longitude], popup=row.gade
        ).add_to(m)
    return m

st.write("Kort over tømninger")

df = read_data()
m = create_map(df)
events = st_folium(m)