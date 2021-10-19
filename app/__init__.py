from flask import Flask
from flask_mail import Mail

app = Flask(__name__)
# Set up the app to use Flask-Mail, for sending emails
mail = Mail(app)

# The secret key here is used for demonstration purposes - DO NOT USE IN PRODUCTION
app.config['SECRET_KEY'] = 'this-is-a-secret' 

# A constant used for common message types for emails
MESSAGE_TYPES = ['Error in activity', 'Assignment Question', 'Troubleshooting help']

from app import routes