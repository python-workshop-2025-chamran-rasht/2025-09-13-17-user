from werkzeug.security import generate_password_hash, check_password_hash
from typing import Optional
from flask import Flask, render_template, redirect, flash, request
from forms import LoginForm, SignupForm
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import sqlalchemy as sa
import sqlalchemy.orm as so
from flask_login import LoginManager, UserMixin, login_user, current_user, login_required, logout_user
from urllib.parse import urlsplit

app = Flask(__name__)

app.config.from_object('default_config')
app.config.from_prefixed_env()

db = SQLAlchemy(app)
migrate = Migrate(app, db)
login_mgr = LoginManager(app)
login_mgr.login_view = 'login_ep'

class User(UserMixin, db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    username: so.Mapped[str] = so.mapped_column(sa.String(64), index=True, unique=True)
    email: so.Mapped[str] = so.mapped_column(sa.String(128), index=True, unique=True)
    password_hash: so.Mapped[str] = so.mapped_column(sa.String(256))

    posts: so.WriteOnlyMapped['Post'] = so.relationship(back_populates='author')

    def __repr__(self) -> str:
        return f"<User {self.username}>"

    def set_password(self, password: str):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password: str):
        return check_password_hash(self.password_hash, password)

@login_mgr.user_loader
def load_user(id):
    return db.session.get(User, int(id))

class Post(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    content: so.Mapped[str] = so.mapped_column(sa.String(512))
    user_id: so.Mapped[int] = so.mapped_column(sa.ForeignKey(User.id), index=True)

    author: so.Mapped[User] = so.relationship(back_populates='posts')

    def __repr__(self) -> str:
        return f"<post {self.content}>"

@app.route('/')
@login_required
def index_ep():
    return render_template('index.html')

@app.route('/logout')
def logout_ep():
    logout_user()
    return redirect('/')

@app.route('/login', methods=['GET', 'POST'])
def login_ep():
    if current_user.is_authenticated:
        return redirect('/')

    form = LoginForm()

    if form.validate_on_submit():
        user = db.session.scalar(sa.Select(User).where(User.username == form.username.data))

        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect('/login')

        login_user(user)

        next_page = request.args.get('next')

        if not next_page or urlsplit(next_page).netloc != '':
            next_page = '/'

        return redirect(next_page)

    return render_template('login.html', form=form)

@app.route('/signup', methods=['GET', 'POST'])
def signup_ep():
    form = SignupForm()

    if form.validate_on_submit():
        flash('You are now signed up.')
        return redirect('/')

    return render_template('signup.html', form=form)
