from flask import Flask, render_template, url_for, redirect
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL, InputRequired
import csv

# with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
#         csv_data = csv.reader(csv_file, delimiter=',')
#         print(csv_data)
#         list_of_rows = []
#         for row in csv_data:
#             list_of_rows.append(row)
#         print(list_of_rows)
'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

class MyInputRequired(InputRequired):
    field_flags = ()

class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[MyInputRequired(), DataRequired()])
    location = StringField("Cafe Location on Google Maps(URL)", validators=[MyInputRequired(), DataRequired(), URL(require_tld=True)])
    # Here, I am adding URL validator that checks that the entered url is valid or not.
    # require_tld checks whether domain name portion of the url contains ".tld" or not.
    opening_time = StringField("Opening Time e.g. 8AM", validators=[MyInputRequired(), DataRequired()])
    closing_time = StringField("Closing Time e.g. 5:30PM", validators=[MyInputRequired(), DataRequired()])
    coffee_rating = SelectField("Coffee Rating", choices=["☕", "☕☕", "☕☕☕", "☕☕☕☕", "☕☕☕☕☕"])
    wifi_rating = SelectField("Wifi Strength Rating", choices=["✘", "💪", "💪💪", "💪💪💪", "💪💪💪💪", "💪💪💪💪💪"])
    power_availability = SelectField("Power Socket Availability", choices=["✘", "🔌", "🔌🔌", "🔌🔌🔌", "🔌🔌🔌🔌", "🔌🔌🔌🔌🔌"])
    submit = SubmitField('Submit')

# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
#e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    my_form = CafeForm()
    return render_template("index.html", form=my_form)


@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        cafe_name = form.cafe.data
        location_name = form.location.data
        open_time = form.opening_time.data
        close_time = form.closing_time.data
        coffee_rating = form.coffee_rating.data
        wifi_rating = form.wifi_rating.data
        power_availability = form.power_availability.data
        new_cafe_details = [cafe_name, location_name, open_time, close_time, coffee_rating, wifi_rating, power_availability]
        with open("cafe-data.csv", "a", encoding='utf-8') as csv_file:
            new_cafe = ",".join(new_cafe_details)
            csv_file.write(f"\n{new_cafe}")
        # with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        #     csv_data = csv.reader(csv_file, delimiter=',')
        #     list_of_rows = []
        #     for row in csv_data:
        #         list_of_rows.append(row)
        # return render_template('cafes.html', cafes=list_of_rows)
        return redirect(url_for('cafes'))
    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
