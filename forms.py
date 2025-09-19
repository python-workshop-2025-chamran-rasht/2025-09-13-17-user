from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    BooleanField,
    SubmitField,
    PasswordField,
    EmailField,
    TelField,
)
from wtforms.validators import DataRequired, Length, Email, Optional, EqualTo, Regexp


class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired(), Length(8)])
    remember_me = BooleanField("Remember me")
    submit = SubmitField("Sign in")


class SignupForm(FlaskForm):
    full_name = StringField("Full name", validators=[DataRequired(), Length(2)])
    email = EmailField(
        "Email address", validators=[DataRequired(), Email(), Regexp(".*@gmail\\.com")]
    )
    phone = TelField(
        "Phone number", validators=[Optional(), Length(12, 12), Regexp("09.*")]
    )
    password = PasswordField(
        "Password", validators=[DataRequired(), Length(8), Regexp(".*[@#$].*")]
    )
    repeat_password = PasswordField(
        "Repeat Password", validators=[DataRequired(), EqualTo("password")]
    )
    submit = SubmitField("Sign up")
