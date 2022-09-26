from data_manager import DataManager
from morse_translator import MorseTranslator
from flask import Flask, jsonify, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap
from beepify import beepify
from flask_wtf import FlaskForm
from wtforms import TextAreaField, HiddenField, SubmitField
from wtforms.validators import DataRequired


app = Flask(__name__)
app.config["SECRET_KEY"] = "8BYkEfBA6O6donzWlSihBXox7C0sKR6b"
Bootstrap(app)


class MorseForm(FlaskForm):
    message = TextAreaField(
        "Message to code", id="message", validators=[DataRequired()]
    )
    morse_code = TextAreaField("Encoded message", id="morse")
    morse_sounds = HiddenField()
    submit = SubmitField("Encode")


data_manager = DataManager()
data_manager.read_data_csv("morse.csv")
translator = MorseTranslator(data_manager)


@app.route("/", methods=["POST", "GET"])
def home():
    form = MorseForm()

    if form.validate_on_submit():
        message_to_encode = form.message.data
        morse = translator.translate(message_to_encode)
        beeps = beepify(morse)

        form.morse_code.data = morse
        form.morse_sounds.data = beeps
    return render_template("index.html", form=form)


# @app.route("/morsify/<message>", methods=["GET"])
# def translate(message: str):
#     morse_code = translator.translate(message)
#     beeps = beepify(morse_code)
#     return jsonify(message=message, morse=morse_code, beeps=beeps), 200


if __name__ == "__main__":
    app.run(debug=True)
