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

st.dataframe(df_beholdere, use_container_width=True)

data_df = pd.DataFrame(
    {
        "Gade": df['gade'],
        "Beholder": df['beholder'],
        "Tømt": [False] * len(df['gade']),
    }
)

myresult = st.data_editor(
    data_df,
    column_config={
        "Tømt": st.column_config.CheckboxColumn(
            "Er der tømt?",
            help="Er tømt?",
            width="medium",
            default=False,
        )
    },
    disabled=["Gade", "Beholder"],
    hide_index=True,
    key="er_tomt",
    use_container_width=True,
)

#st.write("Here's the session state:")
#st.write(st.session_state["er_tomt"]) # 👈 Access the edited data
state = st.session_state["er_tomt"]


def show_not_tomt(state):
    tomt = []
    for key in state['edited_rows']:
        if state['edited_rows'][key]['Tømt'] == True:
            #st.write(data_df['Gade'][key])
            #st.write(data_df['Beholder'][key])
            #st.write(data_df['Tømt'][key])
            #st.write('---')
            tomt.append(key)
    return [x for x in data_df.index if x not in tomt]
    # '''return a list of the rows that are not tømt'''
    # '''return data_df['Gade'][key] for key in state['edited_rows'] if state['edited_rows'][key]['Tømt'] == False'''
    # '''return data_df['Gade'][key] for key in state['edited_rows'] if state['edited_rows'][key]['Tømt'] == False'''
    # '''return dataframe with only the rows that are not tømt'''
    # '''return dataframe with only the rows that are not tømt'''
         

if st.button('Vis ikke-tømte beholdere'):
    result = show_not_tomt(state)

    '''if data_df.index is not in result, show'''

    isinindex = data_df.index.isin(result)
    st.write(data_df[~isinindex])

if st.button('Vis tømte beholdere'):
    result = show_not_tomt(state)
    isinindex = data_df.index.isin(result)
    st.write(data_df[isinindex])

    #'''if not in result, show'''



    #st.write(data_df.loc[result])

    #st.write(data_df.loc[~result])
#show_not_tomt(state)
# data_df.loc
# def show_tomt(state):


#myresult

# for key in state['edited_rows']:
#         st.write(data_df['Gade'][key])
#         st.write(data_df['Beholder'][key])
#         data_df['Tømt'][key] = state['edited_rows'][key]['Tømt']
        

#         st.write(data_df['Tømt'][key])
#         st.write('---')
    
