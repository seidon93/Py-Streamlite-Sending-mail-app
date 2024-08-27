import streamlit as st
from streamlit import button

st.header('Contact Page')

with st.form(key='email_form'):
    user_email = st.text_input("Enter your email address")
    user_mess = st.text_area("Put in your message")
    e_btn = st.form_submit_button('Submit')

    if button:
        print("Email Submitted")
