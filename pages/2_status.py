import streamlit as st
import pandas as pd


@st.cache_data
def load_data():

    df = pd.read_csv('data/mandag_lige_merged.csv')
    return df



df = load_data()

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
         

if st.button('Vis ikke-tømte beholdere'):
    result = show_not_tomt(state)


    isinindex = data_df.index.isin(result)
    st.write(data_df[isinindex])

if st.button('Vis tømte beholdere'):
    result = show_not_tomt(state)
    isinindex = data_df.index.isin(result)
    st.write(data_df[~isinindex])

