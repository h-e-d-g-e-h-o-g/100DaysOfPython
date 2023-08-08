from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random

'''
Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy()
db.init_app(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
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
        dictionary = {}
        # Defining a class method for converting row object into dictionary
        for column in self.__table__.columns:
            # Looping through the column field object of the table.
            # self.__table__columns gives me a list of column field objects.
            dictionary[column.name] = getattr(self, column.name)
            # Here, I am tapping into each column object's name attribute.
            # getattr() is used to get the class attribute's value.
            # For that, we need to pass the object and the attribute whose value we want to obtain.
        return dictionary


@app.route("/")
def home():
    return render_template("index.html")
    

@app.route("/random")
def random_cafe():
    results = db.session.execute(db.select(Cafe).order_by(Cafe.name))
    cafes_list = results.scalars().all()
    cafe_random = random.choice(cafes_list)
    return jsonify(cafe_random.to_dict())
            # Here, cafe_random is representing a random row object taken out of the table.

    # Previously, we are returning templates, but here our server is acting as an API.
    # As, we know, when we request at the API endpoint, it returns us a json data.
    # Therefore, we need to turn the SQLALCHEMY object into json data, this process is called serialization.
    # Flask has serialization built in method called "jsonlify()".

@app.route("/all")
def all_cafes():
    results = db.session.execute(db.select(Cafe).order_by(Cafe.name))
    cafes_list = results.scalars().all()
    cafe_details = []
    for cafe in cafes_list:
        cafe_details.append(cafe.to_dict())
    
    return jsonify(cafes=cafe_details)

@app.route("/search")
def search_cafe():
    location = request.args.get("loc")
    no_data = {
        "Not Found": "Sorry, We don't have a cafe at that location."
    }
    # Through this, we can obtain the parameter passed into the url.
    results = db.session.execute(db.select(Cafe).order_by(Cafe.name).where(Cafe.location==location))
    cafe_result_list = results.scalars().all()

    if cafe_result_list == []:
        return jsonify(error=no_data)
    
    return jsonify([cafe.to_dict() for cafe in cafe_result_list])

@app.route("/add", methods=["GET", "POST"])
def add_cafe():
    if request.method == "POST":
        cafe_name = request.form.get("name")
        cafe_map_url = request.form.get("map_url")
        cafe_img_url = request.form.get("img_url")
        cafe_location = request.form.get("location")
        cafe_seats = request.form.get("seats")
        cafe_has_toilet = bool(request.form.get("has_toilet"))
        cafe_has_wifi = bool(request.form.get("has_wifi"))
        cafe_has_sockets = bool(request.form.get("has_sockets"))
        cafe_can_take_calls = bool(request.form.get("can_take_calls"))
        cafe_coffee_price = request.form.get("coffee_price")

        # Here, we are using request.form.get() for retrieving the data from the form. It is used in POST request.
        # We are not using request.args.get(), because here, we are not retrieving the value from the url.
        # The above is used for GET request.
        new_cafe = Cafe(name=cafe_name, map_url=cafe_map_url, img_url=cafe_img_url, location=cafe_location, seats=cafe_seats, has_toilet=cafe_has_toilet, has_sockets=cafe_has_sockets, has_wifi=cafe_has_wifi, can_take_calls=cafe_can_take_calls, coffee_price=cafe_coffee_price)
        db.session.add(new_cafe)
        db.session.commit()    

        dictionary = {
            "success": "Successfully added the new cafe."
        }

        return jsonify(response=dictionary)

# Difference between put and patch request.
# For example, there is a piece in an entry, that needs to be changed.
# When we make "put" request to the server, we are replacing an entire entry with the new one.
# When we make "patch" request to the server, we are sending a piece of data to replace the piece that needs to be changed.

@app.route("/update-price/<int:cafe_id>", methods=["POST", "GET", "PATCH"])
def update_price(cafe_id):
    new_price = request.args.get("new_price")
    cafe = db.session.get(Cafe, cafe_id)
    if cafe:
        cafe.coffee_price = new_price
        db.session.commit()
        return jsonify(response={"success": "Successfully updated the price."}), 200
    else:
        #404 = Resource not found
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404

@app.route("/report-closed/<int:cafe_id>", methods=["DELETE"])
def delete(cafe_id):
    api_key_authentication = request.args.get("api-key")
    cafe_delete = db.session.get(Cafe, cafe_id)
    if cafe_delete:
        if api_key_authentication == "TopSecretAPIKey":
            db.session.delete(cafe_delete)
            db.session.commit()
            return jsonify(success="The cafe with passed 'id' is deleted from the 'cafes' database."), 200
        else:
            return jsonify(error="Sorry, that's not allowed. Make sure you have the correct api_key."), 403

    else:
        return jsonify(error={"Not Found" : "Sorry, the cafe with that 'id' is not found in the 'cafes' database."}), 404

if __name__ == '__main__':
    app.run(debug=True)
