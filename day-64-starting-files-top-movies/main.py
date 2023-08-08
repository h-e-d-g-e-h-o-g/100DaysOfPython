from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired
import requests
from pprint import pprint

API_KEY = "f06d81b9803706a1be65c1489e534919"
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

db = SQLAlchemy()

app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///movies-list.db"

db.init_app(app=app)
Bootstrap5(app)

header = {
    "accept": "application/json",
    "Authorization": "Bearer f06d81b9803706a1be65c1489e534919"
}



class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(1000), nullable=False)
    rating = db.Column(db.String, nullable=False)
    ranking = db.Column(db.Integer, nullable=False)
    review = db.Column(db.String(1000), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)

# with app.app_context():
#     db.create_all()

class EditForm(FlaskForm):
    new_rating = FloatField(label="You Rating Out of 10 e.g. 7.5", validators=[DataRequired()])
    new_review = StringField(label="Your Review", validators=[DataRequired()])
    submit = SubmitField(label="Done")

class AddForm(FlaskForm):
    movie_title = StringField("Movie Title", validators=[DataRequired()])
    add_movie = SubmitField("Add Movie")

@app.route("/")
def home():
    movies_obj = db.session.execute(db.select(Movie).order_by(Movie.rating)).scalars()
    movies_list = movies_obj.all()
    
    for num in range(len(movies_list)):
        movies_list[num].ranking = len(movies_list) - num
    # for movie in movies_list:
    #     ranking = ranking + 1
    #     movie.ranking = ranking
    db.session.commit()
    return render_template("index.html", movies=movies_list)

@app.route("/add", methods=["GET", "POST"])
def add():
    add_form = AddForm()
    if request.method == "POST":
        if add_form.validate_on_submit():
            movie_url = "https://api.themoviedb.org/3/search/movie"
            query = {
                "api_key": API_KEY,
                "query": add_form.movie_title.data
            }
            response = requests.get(url=movie_url, params=query, headers=header)
            response_data = response.json()
            results = response_data['results']
            pprint(results)
            return render_template('select.html', results=results)

    return render_template('add.html', form=add_form)
    
#     second_movie = Movie(
#         title="Avatar The Way of Water",
#         year=2022,
#         description="Set more than a decade after the events of the first film, learn the story of the Sully family (Jake, Neytiri, and their kids), the trouble that follows them, the lengths they go to keep each other safe, the battles they fight to stay alive, and the tragedies they endure.",
#         rating=7.3,
#         ranking=9,
#         review="I liked the water.",
#         img_url="https://image.tmdb.org/t/p/w500/t6HIqrRAclMCA60NsSmeqe9RmNV.jpg"
# )

#     db.session.add(second_movie)
#     db.session.commit()

@app.route('/edit', methods=["GET", "POST"])
def edit():
    my_form = EditForm()
    movie_id = request.args.get("id")
    # In order to get the parameter from the url, we use request.args.get("parameter")
    movie_edit = db.get_or_404(Movie, movie_id)
    if request.method == "POST":
        if my_form.validate_on_submit():
            movie_edit.rating = my_form.new_rating.data
            movie_edit.review = my_form.new_review.data
            db.session.commit()

            return redirect(url_for('home'))

    return render_template('edit.html', movie_form=my_form)

@app.route('/delete')
def delete():
    movie_id = request.args.get('id')
    movie_delete = db.get_or_404(Movie, movie_id)
    db.session.delete(movie_delete)
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/info')
def get_info():
    movie_id = int(request.args.get('id'))
    details_url = f"https://api.themoviedb.org/3/movie/{movie_id}"
    params = {
            "api_key": API_KEY
        }
    response = requests.get(url=details_url, params=params, headers=header)
    response_data = response.json()
    movie_title = request.args.get('title')
    movie_year = request.args.get('year')
    movie_description = response_data['overview']
    movie_poster = f"https://www.themoviedb.org/t/p/original/{response_data['poster_path']}"
    movie_ranking = "None"
    movie_review = "None"
    movie_rating = "None"
    add_movie = Movie(title=movie_title, year=movie_year, ranking=movie_ranking, review=movie_review, rating=movie_rating, description=movie_description, img_url=movie_poster)
    db.session.add(add_movie)
    db.session.commit()
    return redirect(url_for('edit', id=add_movie.id))

if __name__ == '__main__':
    app.run(debug=True)
