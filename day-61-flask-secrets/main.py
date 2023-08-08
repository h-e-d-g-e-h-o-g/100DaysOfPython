from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email

app = Flask(__name__)
bootstrap = Bootstrap5(app=app)

# Initializing bootstrap-flask in our flask application

app.config['SECRET_KEY'] = 'Arpit26@'
# Here, we have created secret key to generate csrf_token to provide csrf protection to the website
'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''
class MyForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(), Email(message="Invalid email address.")])
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=8, max=16, message="Field must be at least 8 characters long.")])
    submitButton = SubmitField(label='Log In')

# FlaskForm is a parent class, and MyForm is a class that is inheriting from the parent class such as its attributes and methods.

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=["GET", "POST"])
def login():
    my_form = MyForm()
    if my_form.validate_on_submit():
        if my_form.email.data == "admin@email.com" and my_form.password.data == "12345678":
            # we can access the data on the email field through form_object.field_name.data
            # Here, we are confirming the form data is successfully validated or not.
            # validate_on_submit() gives return value as True(form data is successfully validated) or False(failed)
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template("login.html", form=my_form)

# Now, we want our form to validate the user's input after he hits the submit button.
# To catch post request, we are adding methods argument.
# Using validate_on_submit(), our form would be able to validate the entries as per the validators we have set.
# We would get pop up and telling us to fill the field.
# This pop up is coming from browser not from our validators.
# The pop up message varies from browser to browser, therefore each user might get different messages.
# To avoid it, and to give same messages to all users, we need to add "novalidate" attribute to the form element.

if __name__ == '__main__':
    app.run(debug=True)
