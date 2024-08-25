import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("Images/photo.png")

with col2:
    st.title("Jméno autora")
    author_text = """Ahoj to jsme já a hodlám se tu představit."""
    st.info(author_text)