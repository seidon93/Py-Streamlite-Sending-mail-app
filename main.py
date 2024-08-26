import streamlit as st
import pandas as pd
st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("Images/me.png" )

with col2:
    st.title("Jméno autora")
    author_text = """Ahoj to jsme já a hodlám se tu představit."""
    st.info(author_text)

cont1 = st.container()
cont1.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse luctus neque ut posuere lacinia. Vivamus semper non ante sit amet aliquet. Nam vitae nisi ante. Quisque nec ornare nisl. Vestibulum a felis a lacus vehicula vehicula.")


col3, col4 = st.columns(2)

df = pd.read_csv("data.csv", sep=";")
with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])