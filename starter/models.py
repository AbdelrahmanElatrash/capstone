from datetime import date
import os
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String , Date ,exc
import sys



database_path = os.environ['DATABASE_URL']
if database_path.startswith("postgres://"):
  database_path = database_path.replace("postgres://", "postgresql://", 1)

db=SQLAlchemy()

def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()


class Mixin:

    def save_to_db(self):
        try:
            db.session.add(self)
            db.session.commit()
            return {"error": False}
        except exc.SQLAlchemyError as e:
            print(e)
            print(sys.exc_info())
            db.session.rollback()
            return {"error": True}
        #finally:
            #db.session.close()
    
    def delete_from_db(self):
        try:
            db.session.delete(self)
            db.session.commit()
            return {"error": False}
        except exc.SQLAlchemyError as e:
            print(e)
            print(sys.exc_info())
            db.session.rollback()
            return {"error": True}
        #finally:
            #db.session.close()

    def update(self):
        db.session.commit()
    
    
# many to many relationship 
movies_actors= db.Table('movies_actors' , 
                        db.Column('movies_id', db.Integer, db.ForeignKey('movies.id')),
                        db.Column('actors_id', db.Integer, db.ForeignKey('actors.id'))
                       )


class Movies(db.Model, Mixin):
    __tablename__ ='movies'
    id=db.Column(db.Integer, primary_key=True)
    title=Column(String)
    release_date=db.Column(db.Date)
    actors= db.relationship( "Actors", secondary='movies_actors', backref="movies" , lazy=True)


    def __init__(self,title,release_date):
        self.title= title
        self.release_date= release_date

    def format(self):
        return {
            'id' : self.id ,
            'title': self.title,
            'release date': self.release_date
            
        }
    

    

    

class Actors(db.Model, Mixin):
    __tablename__ ='actors'
    id=db.Column(db.Integer, primary_key=True)
    name=Column(String)
    date_of_birth=db.Column(db.Date)
    gender=Column(String)

    def __init__(self,name,date_of_birth,gender):
        self.name= name
        self.date_of_birth= date_of_birth
        self.gender= gender
        
    def format(self):
        return {
      'id': self.id,
      'name': self.name,
      'date_of_birth': self.date_of_birth,
      'gender': self.gender
    }
