from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField, TextAreaField, PasswordField, BooleanField
from wtforms.validators import DataRequired

class EmailForm(FlaskForm):
    first_name = StringField('Ime', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired()])
    message = TextAreaField('Poruka', validators=[DataRequired()])
    submit = SubmitField('Posalji')

class LoginForm(FlaskForm):
    username = StringField('Korisničko ime', validators=[DataRequired()])
    password = PasswordField('Šifra', validators=[DataRequired()])
    remember_me = BooleanField('Zapamti me')
    submit = SubmitField('Potvrdi')