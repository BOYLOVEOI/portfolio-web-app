# Import statements 
# smtplib library will allow us to send reply e-mails 
# ssl is required to create a secure context for the security of the contents of our e-mails and to
# provide security from MITM attacks
import smtplib, ssl

# Importing os, to retrieve the e-mail password stored in an environment variable
import os

# Creating a function to be imported and utilized when the submit button is pressed
def send_email(message):
    # Host (in our case g-mail, as we will be sending e-mails through g-mail) and smtp.gmail.com is the server that
    # sends e-mails of g-mail users on their behalf
    host = "smtp.gmail.com"

    # Port 465 -> Port 465 is commonly associated with SMTPS
    port = 465

    # Creating a secure context to send e-mails securely (especially for the user)
    context = ssl.create_default_context()

    # G-mail username
    user_name = "plavoieportfolio@gmail.com"
    # G-mail app password from the environment variable PASSWORD through the os.getenv() method
    password = os.getenv("PASSWORD")

    # Test purposes
    receiver = "plavoieportfolio@gmail.com"
    
    # Creating an smtplib.STMP_SSL object with the 'with' context manager and naming it server
    with smtplib.SMTP_SSL(host=host, port=port, context=context) as server:
        # Logging in to my e-mail with the credentials stored in variables user_name and password
        server.login(user=user_name, password=password)

        # Sending e-mail
        server.sendmail(from_addr=user_name, to_addrs=receiver, msg=message)

