# misy350-project

What this project does is create a list of directors and wit them there will be
a list of movies the have directed.

The database design is simple, having two table. Those tables being Directors
and movies. With Directors having a one-to-many relationship with Movies and
Movies has a one-to-one relationship with Directors.

Directors Database looks like:


Director Name | About
------------ | -------------
Director 1 | About Director 1
Director 2 | About Director 1


Movies Database looks like:

Movie Name | Director | Release Date
------------ | ------------- | -------------
Movie 1 |  Director 1 | Release Date of Movie 1
Movie 2 |  Director 2 | Release Date of Movie 2


To run this you must first have done the following:

Install `virtualenv venv`

The activate the virtual environment by typing (in Windows powershell):

```
venv/scripts/activate
```
