from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, TextAreaField
from wtforms.validators import InputRequired

class NewMessageForm(FlaskForm):
    ''' Form for creating and sending an email message '''
    sender = StringField('Sender (name):', validators=[InputRequired()])
    message_type = SelectField('Message type:', validators=[InputRequired()])
    message = TextAreaField('Message:', validators=[InputRequired()])
    submit = SubmitField('Send')

