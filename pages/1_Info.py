import streamlit as st
import pandas as pd
import os
import sys

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))



st.set_page_config(page_title="Info", page_icon=":house:")
st.write("# Info")
csv_file = 'data/mandag_ulige_merged.csv'

@st.cache_data
def load_data(data):
    data = pd.read_csv(data)
    #lowercase = lambda x: str(x).lower()
    #data.rename(lowercase, axis='columns', inplace=True)
    #'''cast column "postnr" to string'''
    data['postnr'] = data['postnr'].astype(str)
    data = data.drop(columns=['tur'])
    data['nr'] = data['gade'].str.extract('(\d+)').astype(int)
    #data['gade'] = data['gade'].str.replace('\d+', '')
    data['gade'] = data['gade'].str.extract('(\D+)').astype(str)
    data.sort_values(by = ['gade', 'nr', 'beholder'], ascending = True, inplace=True)

    #return_data = data.groupby(['gade', 'postnr', 'beholder'])['antal'].sum(numeric_only=True).reset_index()
    return_data = data
    #'''return data where antal is greater than 0'''
    #return_data = return_data[return_data['antal'] > 0]
    #return_data = return_data['antal']
    return return_data



# Create a text element and let the reader know the data is loading.
#data_load_state = st.text('Loading data...')
# Load 10,000 rows of data into the dataframe.
raw_data = load_data(csv_file)
# Notify the reader that the data was successfully loaded.
#data_load_state.text('Loading data...done!')


tab1, tab2 = st.tabs(['Info', 'Andet'])

with tab1:

    st.write('## Info')

    st.write('### Mandag ulige')
    st.write('Tømninger:')
    antal = raw_data['antal'].sum()
    st.write(f'Antal: {antal}')
        #st.write(raw_data['antal'].sum())


    st.text('Fordelt på følgende størrelser(antal i liter):')
    antal_type = raw_data.groupby(['type'])[["antal"]].sum(numeric_only=True).reset_index()

    antal_type = antal_type.set_index('type')
    st.write(antal_type.T)

    st.divider()

    st.write('Sække til ombytning:')
    antal_sække = raw_data[raw_data['sæk']].groupby(['gade', 'nr','postnr', 'beholder', 'fremsætter'])['antal'].sum(numeric_only=True).reset_index()
    st.write(f' Antal: {raw_data["sæk"].sum()}')
        #sække = raw_data[raw_data['sæk']]
    if st.checkbox('Vis Adresser_1'):
            
        #st.write(sække[['gade', 'postnr', 'antal', 'beholder', 'fremsætter']])
        #st.write(antal_sække)
        st.dataframe(antal_sække, use_container_width=True)

    st.divider()

    st.write('Fremsætninger:')
    antal_fremsætninger = raw_data[raw_data['fremsætter']].groupby(['gade', 'nr','postnr', 'beholder'])['antal'].sum(numeric_only=True).reset_index()
    st.write(f' Antal: {raw_data["fremsætter"].sum()}')
    if st.checkbox('Vis Adresser_2'):
        #st.write(antal_fremsætninger)
        st.dataframe(antal_fremsætninger, use_container_width=True)
        # antal_fremsætninger = raw_data.groupby(['fremsætter'])[["antal"]].sum(numeric_only=True).reset_index()
        # antal_fremsætninger = antal_fremsætninger.set_index('fremsætter')
        # st.write(antal_fremsætninger.T)



        # Antal = raw_data['antal'].sum()
        # st.write(f'Antal: {Antal}')
    # if st.checkbox('Show raw data'):
    #     st.subheader('Raw data')
    #     st.write(raw_data)

