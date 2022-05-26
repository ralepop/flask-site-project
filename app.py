from flask import Flask, render_template, flash, redirect, url_for
from forms import EmailForm, LoginForm
import smtplib
from os import environ

app = Flask(__name__)



app.config['SECRET_KEY'] = 'todor-petkovic'
app.config['SENSITIVE_PASSWORD'] = environ.get('SENSITIVE_PASSWORD')


@app.route('/')
def index():
    return render_template('index.html', title='Home')

@app.route('/form', methods=['GET', 'POST'])
def form():
    form = EmailForm()
    if form.validate_on_submit():
        flash(f'Ime: {form.first_name.data}')
        flash(f'Email: {form.email.data}')
        flash(f'Poruka: {form.message.data}')
        message = form.message.data
        email = form.email.data
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login('ralespam04@gmail.com', app.config['SENSITIVE_PASSWORD'])
        server.sendmail('ralespam04@gmail.com', email, message)
        return redirect(url_for('index'))

    return render_template('form.html', title='Email', form=form, mail_sender='ralespam04@gmail.com')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if(form.validate_on_submit()):
        flash(f'Korisničko ime: {form.username.data}')
        flash(f'Šifra: {form.password.data}')
        return redirect(url_for('index'))
    
    return render_template('login.html', title='Login', form=form)
    