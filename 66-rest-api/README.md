# Learnings

## Library `jsonify`

`jsonify` is a function in Flask's `flask.json` module. `jsonify` serializes data to JavaScript Object Notation (JSON) format, wraps it in a Response object with the application/json mimetype.

## Search for a obhect in SQLAlchemy

`all_cafes = Cafe.query.filter_by(location=search_location).all()`

## API App

```python
from flask import Flask, jsonify, render_template, request
from dataclasses import dataclass
from flask_sqlalchemy import SQLAlchemy
import random
import os

app = Flask(__name__)

# Connect to Database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///cafes.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

api_key = os.environ.get("SECRET_FLASK_KEY")

# Cafe TABLE Configuration
# @dataclass
class Cafe(db.Model):
    # id: int
    # name: str
    # map_url: str
    # img_url: str
    # location: str
    # seats: str
    # has_toilet: bool
    # has_wifi: bool
    # has_sockets: bool
    # can_take_calls: bool
    # coffee_price: str
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        # Method 1.
        dictionary = {}
        # Loop through each column in the data record
        for column in self.__table__.columns:
            # Create a new dictionary entry;
            # where the key is the name of the column
            # and the value is the value of the column
            dictionary[column.name] = getattr(self, column.name)
        return dictionary

    # Method 2. Altenatively use Dictionary Comprehension to do the same thing.
    # return {
    #     column.name: getattr(self, column.name) for column in self.__table__.columns
    # }

@app.route("/")
def home():
    return render_template("index.html")

# HTTP GET - Read Record
@app.route("/random", methods=["GET"])
def get_random():
    all_cafes = Cafe.query.all()
    random_cafe = random.choice(all_cafes)
    return jsonify(
        cafe={
            "id": random_cafe.id,
            "name": random_cafe.name,
            "map_url": random_cafe.map_url,
            "img_url": random_cafe.img_url,
            "location": random_cafe.location,
            "seats": random_cafe.seats,
            "has_toilet": random_cafe.has_toilet,
            "has_wifi": random_cafe.has_wifi,
            "has_sockets": random_cafe.has_sockets,
            "can_take_calls": random_cafe.can_take_calls,
            "coffee_price": random_cafe.coffee_price,
        }
    )

@app.route("/all", methods=["GET"])
def get_all():
    all_cafes = Cafe.query.all()
    return jsonify(cafes=[cafe.to_dict() for cafe in all_cafes])

@app.route("/search", methods=["GET"])
def search():
    search_location = request.args.get("location")
    all_cafes = Cafe.query.filter_by(location=search_location).all()
    if all_cafes:
        return jsonify(cafes=[cafe.to_dict() for cafe in all_cafes])
    else:
        return jsonify(
            error={"Not found": "Sorry, we dont have a cafe at that location"}
        )

# HTTP POST - Create Record
# For URL query parameters, use request.args.
# For posted form input, use request.form.
@app.route("/add", methods=["POST"])
def post_new_cafe():
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("loc"),
        has_sockets=bool(request.form.get("sockets")),
        has_toilet=bool(request.form.get("toilet")),
        has_wifi=bool(request.form.get("wifi")),
        can_take_calls=bool(request.form.get("calls")),
        seats=request.form.get("seats"),
        coffee_price=request.form.get("coffee_price"),
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})

# HTTP PUT/PATCH - Update Record
@app.route("/update-price/<int:id>", methods=["PATCH"])
def patch_new_price(id):
    new_price = request.form.get("new_price")
    cafe = db.session.query(Cafe).get(id)
    if cafe:
        cafe.coffee_price = new_price
        db.session.commit()
        # Just add the code after the jsonify method. 200 = Ok
        return jsonify(response={"success": "Successfully updated the price."}), 200
    else:
        # 404 = Resource not found
        return (
            jsonify(
                error={
                    "Not Found": "Sorry a cafe with that id was not found in the database."
                }
            ),
            404,
        )

# HTTP DELETE - Delete Record
@app.route("/report-closed/<int:id>", methods=["DELETE"])
def delete_cafe(id):
    key = request.form.get("api_key")
    if key == api_key:
        cafe = db.session.query(Cafe).get(id)
        if cafe:
            db.session.delete(cafe)
            db.session.commit()
            return (jsonify(response={"success": "Successfully deleted cafe."}), 200)
        else:
            return (
                jsonify(
                    error={
                        "Not Found": "Sorry a cafe with that id was not found in the database."
                    }
                ),
                404,
            )
    else:
        # 404 = Resource not found
        return (
            jsonify(error={"Forbidden": "Your api key is not correct"}),
            401,
        )

if __name__ == "__main__":
    app.run(debug=True)
```
