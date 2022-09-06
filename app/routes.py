from app import app
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm
from flask_babel import _

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Vova'}
    posts = [
        {
            'author': {'username': _('John')},
            'body': _('Beautiful day in Portland!')
        },
        {
            'author': {'username': _('Susan')},
            'body': _('The Avengers movie was so cool!')
        },
        {
            'author': {'username': _('Ипполит')},
            'body': _('Какая гадость эта ваша заливная рыба!!')
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)