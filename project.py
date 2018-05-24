import os
from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
db = SQLAlchemy(app)

class Director(db.Model):
    __tablename__='directors'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64))
    about = db.Column(db.Text)
    movies = db.relationship('Movie', backref='director', cascade='delete')

class Movie(db.Model):
    __tablename__='movies'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64))
    budget = db.Column(db.String(64))
    directorid = db.Column(db.Integer, db.ForeignKey('directors.id'))


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/directors')
def all_directors():
    directors = Director.query.all()
    return render_template('all-directors.html', directors=directors)

@app.route('/director/edit/<int:id>', methods=['GET', 'POST'])
def director(id):
    director = Director.query.filter_by(id=id).first()

    if request.method == 'GET':
        return render_template('director-edit.html', director=director)

    if request.method == 'POST':
        director.name = request.form['name']
        director.about = request.form['about']
        db.session.commit()
        return redirect(url_for('all_directors'))

@app.route('/director/add', methods=['GET', 'POST'])
def add_directors():
    if request.method == 'GET':
        return render_template('add-director.html')
    if request.method == 'POST':
        name = request.form['name']
        about = request.form['about']

        director = Director(name=name, about=about)
        db.session.add(director)
        db.session.commit()
        return redirect(url_for('all_directors'))

@app.route('/director/delete/<int:id>', methods=['GET', 'POST'])
def delete_director(id):
    director = Director.query.filter_by(id=id).first()
    if request.method == 'GET':
        return render_template('delete-director.html', director=director)
    if request.method == 'POST':
        db.session.delete(director)
        db.session.commit()
        return redirect(url_for('all_directors'))

@app.route('/movies')
def all_movies():
    movies = Movie.query.all()
    return render_template('all-movies.html', movies=movies)

@app.route('/movie/add', methods=['GET', 'POST'])
def add_movie():
    if request.method == 'GET':
        directors = Director.query.all()
        return render_template('add-movie.html', directors=directors)
    if request.method == 'POST':
        name = request.form['name']
        budget = request.form['budget']
        director_name = request.form['director']
        director = Director.query.filter_by(name=director_name).first()
        movie = Movie(name=name, budget=budget, director=director)
        db.session.add(movie)
        db.session.commit()
        return redirect(url_for('all_movies'))

@app.route('/movie/edit/<int:id>', methods=['GET', 'POST'])
def edit_movie(id):
    movie = Movie.query.filter_by(id=id).first()
    directors = Director.query.all()
    if request.method == 'GET':
        return render_template('movie-edit.html', movie=movie, directors=directors)
    if request.method == 'POST':
        movie.name = request.form['name']
        movie.budget = request.form['budget']
        director_name = request.form['director']
        director = Director.query.filter_by(name=director_name).first()
        movie.director = director
        db.session.commit()
        return redirect(url_for('all_movies'))

@app.route('/movie/delete/<int:id>', methods=['GET', 'POST'])
def delete_movie(id):
    movie = Movie.query.filter_by(id=id).first()
    directors = Movie.query.all()
    if request.method == 'GET':
        return render_template('delete-movie.html', movie=movie, directors=directors)
    if request.method == 'POST':
        db.session.delete(movie)
        db.session.commit()
        return redirect(url_for('all_movies'))


if __name__ == '__main__':
    app.run()
