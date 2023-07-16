import streamlit as st

#create a title for your app
st.title('House Price Data Analysis') 
st.subheader('About this app')

st.markdown(""" 
This app performs simple data analysis on the ***House Price*** dataset.
* **Python libraries:**
    - pandas
    - streamlit
    - numpy
    - matplotlib
    - seaborn
* **Data Source:** [Kaggle]()    
            
            
            
        """, unsafe_allow_html= True)