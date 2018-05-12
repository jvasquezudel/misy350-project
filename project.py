import os
from flask import Flask, render_template, request
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


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/directors')
def all_artists():
    directors = Director.query.all()
    return render_template('all-directors.html', directors=directors)

@app.route('/director/edit/<int:id>')
def director_edit(id):
    director = Director.query.filter_by(id=id).first()
    director.about = "The director is"
    db.session.commit()
    return "The director %d is updated" % id


if __name__ == '__main__':
    app.run()
