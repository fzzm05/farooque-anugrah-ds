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

#display the dataset
if st.checkbox('Show Dataset', True):
    st.subheader('dataset')
    st.dataframe(df)