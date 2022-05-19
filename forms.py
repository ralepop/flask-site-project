from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField, TextAreaField
from wtforms.validators import DataRequired

class EmailForm(FlaskForm):
    first_name = StringField('Ime', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired()])
    message = TextAreaField('Poruka', validators=[DataRequired()])
    submit = SubmitField('Posalji')
