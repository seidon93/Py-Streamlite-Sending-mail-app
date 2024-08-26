import streamlit as st
import pandas as pd
from click import style
from streamlit import caption

st.set_page_config(layout="wide")

c = st.container()
c.title("The example Company")
c.write("Lorem ipsum" * 35)

c.header("Our team")

col1, col2, col3 = st.columns(3)

csv =  pd.read_csv("2/data.csv")


with col1:
    for index, row in csv[:4].iterrows():
        st.subheader(f'{row["first name"].title()} {row["last name"].title()}')
        st.write(row["role"])
        st.image("2/images/" + row["image"])

with col2:
    for index, row in csv[4:8].iterrows():
        st.subheader(f'{row["first name"].title()} {row["last name"].title()}')
        st.write(row["role"])
        st.image("2/images/" + row["image"])

with col3:
    for index, row in csv[8:].iterrows():
        st.subheader(f'{row["first name"].title()} {row["last name"].title()}')
        st.write(row["role"])
        st.image("2/images/" + row["image"])

