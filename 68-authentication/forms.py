from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Email


class RegisterForm(FlaskForm):
    email = StringField(label="Name", validators=[DataRequired(), Email()])
    name = StringField(label="Name", validators=[DataRequired()])
    password = StringField(label="Name", validators=[DataRequired()])


class LoginForm(FlaskForm):
    email = StringField(label="Name", validators=[DataRequired(), Email()])
    password = StringField(label="Name", validators=[DataRequired()])
