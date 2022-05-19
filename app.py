from flask import Flask, render_template, flash, redirect
from forms import EmailForm
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
        server.login('ovde mejl sa kod saljes', app.config['SENSITIVE_PASSWORD'])
        server.sendmail('ovde mejl sa kod saljes', email, message)
        return redirect('/')

    return render_template('form.html', title='Email', form=form)
