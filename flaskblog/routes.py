from flask import render_template, url_for, flash, redirect
from flaskblog import app
from flaskblog.forms import RegistrationFrom, LoginForm
from flaskblog.models import User, Post

posts = [
    {
        'title': 'Article 1',
        'author': 'Ashish Deora',
        'date_posted': '23rd April 2020',
        'content': 'Hello world'
    },
    {
        'title': 'Article 2',
        'author': 'Vinay Makwana',
        'date_posted': '24th April 2020',
        'content': 'Hello world again'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationFrom()
    if form.validate_on_submit():
        flash(f'User has been created with username {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'ashish@gmail.com' and form.password.data == 'Password':
            flash(f'You have successfully logged in', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)
