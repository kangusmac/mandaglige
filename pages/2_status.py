import streamlit as st
import pandas as pd

st.set_page_config(page_title="Status", page_icon=":house:")
st.write("## Status")
csv_file = 'data/mandag_ulige_merged.csv'


@st.cache_data
def load_data():

    df = pd.read_csv('data/mandag_ulige_merged.csv')
    df['nr'] = df['gade'].str.extract('(\d+)').astype(int)
    df['gade'] = df['gade'].str.extract('(\D+)').astype(str)
    df['gade'] = df['gade'].str.replace('\d+', '')
    df.sort_values(by=['gade', 'nr', 'beholder'], inplace=True)
    return df



df = load_data()

df_tomt = df.groupby(['gade', 'nr', 'beholder'])['antal'].sum().reset_index()
df_tomt['tømt'] = False

# data_df = pd.DataFrame(
#     {
#         "Gade": df['gade'],
#         "Beholder": df['beholder'],
#         "Tømt": [False] * len(df['gade']),
#     }
# )
# data_df.sort_values(by=['Gade', 'Beholder'], inplace=True)

myresult = st.data_editor(
    df_tomt,
    column_config={
        "tømt": st.column_config.CheckboxColumn(
            "Er der tømt?",
            help="Er tømt?",
            width="medium",
            default=False,
        
        ),
        "gade": st.column_config.TextColumn(
            "Gade",
            help="Gade",
            width="medium",
            default=False,
        
        )
    },
    disabled=["gade", 'nr', "beholder"],
    hide_index=True,
    key="er_tomt",
    use_container_width=False,
)

#st.write("Here's the session state:")
#st.write(st.session_state["er_tomt"]) # 👈 Access the edited data
state = st.session_state["er_tomt"]


def show_not_tomt(state):
    tomt = []
    for key in state['edited_rows']:
        if state['edited_rows'][key]['tømt'] == True:
            #st.write(data_df['Gade'][key])
            #st.write(data_df['Beholder'][key])
            #st.write(data_df['Tømt'][key])
            #st.write('---')
            tomt.append(key)
    return [x for x in df_tomt.index if x not in tomt]
         

if st.button('Vis ikke-tømte beholdere'):
    result = show_not_tomt(state)


    isinindex = df_tomt.index.isin(result)
    st.write(df_tomt[isinindex])

if st.button('Vis tømte beholdere'):
    result = show_not_tomt(state)
    isinindex = df_tomt.index.isin(result)
    st.write(df_tomt[~isinindex])

