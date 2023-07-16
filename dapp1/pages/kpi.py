import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px

#loading the data

@st.cache_data
def load_data():
    path = 'data/kc_house_data.csv'
    df = pd.read_csv(path)
    return df

#call the load_data function
with st.spinner('loading data/..'):
    df = load_data()

#create a title for your app
st.title('House Price data Analysis')
df= load_data()

#display the dataset
if st.checkbox('Show Dataset', True):
    st.subheader('dataset')
 
#get the list of all columns
cols = df.columns.tolist()
selected_cols = st.multiselect('Select Columns', cols)
st.write(f'You selected: {len(selected_cols)} columns')

for col in selected_cols:
    try:
        st.metric(label=f'Mean {col}',
                value=round(df[col].mean()),
                delta=round(df[col].std()))
        st.line_chart(df[col], use_container_width= True)
    except:
        st.error(f'Cannot Display {col} Numeric Data')