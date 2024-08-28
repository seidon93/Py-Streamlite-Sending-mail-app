import streamlit as st
from Send_mail import send_email

st.header('Contact Page')

with st.form(key='email_form'):
    user_email = st.text_input("Enter your email address")
    user_mess = st.text_area("Put in your message")
    message = f"""\n
    Subject: New email from {user_email}
    From: {user_email}
    {user_mess}
    """
    button = st.form_submit_button("Submit")
    if button:
        print("Email Submitted")
        send_email(message)
        st.info('Email was sent!')

