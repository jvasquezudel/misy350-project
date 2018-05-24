from flask_script import Manager
from project import app, db, Director, Movie

manager = Manager(app)

@manager.command
def deploy():
    print "reseting database"
    db.drop_all()
    db.create_all()

    print "inserting initial data..."
    director1 = Director(name="Ryan Coogler", about="Director of Black Panther")
    director2 = Director(name="Anthony Russo and Joe Russo", about="Directors of Avengers: Infinity War")
    director3 = Director(name="David Leitch", about="Director of Deadpool 2")

    movie1 = Movie(name="Black Panther", budget="$200 Million", director=director1)
    movie2 = Movie(name="Avengers: Infinity War", budget="$400 Million", director=director2)
    movie3 = Movie(name="Deadpool 2", budget="$110 Million", director=director3)

    db.session.add(director1)
    db.session.add(director2)
    db.session.add(director3)

    db.session.add(movie1)
    db.session.add(movie2)
    db.session.add(movie3)

    db.session.commit()


if __name__ == '__main__':
    manager.run()
