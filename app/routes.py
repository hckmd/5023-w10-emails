from flask import render_template
from flask_mail import Message

from app import app, mail, MESSAGE_TYPES
from app.forms import NewMessageForm

@app.route('/', methods = ['GET', 'POST'])
def email_message():

    # Create the form with the message type constants as select options
    form = NewMessageForm()
    form.message_type.choices = MESSAGE_TYPES

    # The form has been completed with appropriate inputs
    if form.validate_on_submit():

        # Set up variables from the form inputs for the email
        sender_name = form.sender.data
        message_type = form.message_type.data
        message = form.message.data
        email_title = f'{sender_name}: {message_type}'

        # Create an email message for sending to daniel
        email = Message (
            email_title,
            sender ='form@flaskdemos.com',
            recipients=['daniel.hickmott@sydney.edu.au'],
            body = message
        )
        # Send the email through Flask-Mail
        mail.send(email)

        # Show a view with the details of the sent email message
        return render_template('sent_message.html', 
            title = 'Sent Message', 
            email_title = email_title,
            message = message
        )

    # If there is a GET request or there are errors in the form, show the view with form
    return render_template('new_message.html', title = 'New Message', form = form)
