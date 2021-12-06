import streamlit as st
import pandas as pd
import numpy as np
st.title('Uber pickups in NYC')

st.write(
   "header"
)

st.checkbox('checkbox')
add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)
st.write(add_selectbox)

st.image(https://lufiplaza.hu/wp-content/uploads/2020/07/2294202.jpg)