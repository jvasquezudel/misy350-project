from flask_script import Manager
from project import app, db, Director

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

    db.session.add(director1)
    db.session.add(director2)
    db.session.add(director3)

    db.session.commit()


if __name__ == '__main__':
    manager.run()
