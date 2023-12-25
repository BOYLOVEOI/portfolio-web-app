# Import Statements
import streamlit as st
from send_email import send_email

# Title
st.header("Contact Me")

# Creating a form object for users to input their e-mail and message
with st.form(key="email_form"):
    # Creating user input box for e-mail and storing value in user_email
    user_email = st.text_input(label="Your E-mail Address: ", placeholder="Enter in your e-mail address")
    # Creating user input box for message and storing value in user_message
    user_message = st.text_area(label="Your Message: ", placeholder="Enter in your message")
    # Reformatting user_message to be processed as a parameter for send_email() method
    user_message = f"""\
Subject: E-mail from {user_email}

{user_message}

From: {user_email}"""

    # Creating the submit button (specifically for the submission of a form)
    button = st.form_submit_button()

    # If submit button is pressed (as button returns a boolean)
    if button:
        send_email(user_message)
        # Creating an st.info() component to create a informational message to indicate that e-mail has been sent
        st.info("Your e-mail has been sent!")


