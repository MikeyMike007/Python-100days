from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField
from wtforms.validators import DataRequired, Email, Length


class LoginForm(FlaskForm):
    email = StringField(
        label="Email", validators=[DataRequired(), Length(min=6, max=30), Email()]
    )
    password = StringField(label="Password", validators=[DataRequired()])
    submit = SubmitField(label="Log in")


app = Flask(__name__)
app.secret_key = "hello"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    # If validation is OK!
    if login_form.validate_on_submit():
        # Tap into data sent
        print(login_form.email.data)
        print(login_form.password.data)

        if (
            login_form.email.data == "admin@admin.com"
            and login_form.password.data == "123"
        ):
            return render_template("success.html", form=login_form)

        else:
            return render_template("denied.html", form=login_form)

    return render_template("login.html", form=login_form)


if __name__ == "__main__":
    app.run(debug=True)
