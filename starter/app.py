from asyncio import run_coroutine_threadsafe
import os
from flask import Flask, request, abort, jsonify , json
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import setup_db , Movies , Actors 
from auth import AuthError, requires_auth


PER_PAGE = 10

def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  setup_db(app)
  CORS(app)


  # request handeler ----------------------------------------------------------------------------------
  @app.after_request
  def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization, true')
        response.headers.add('Access-Control-Allow-Methods', 'GET, POST, PATCH, DELETE, OPTIONS')
        return response
  

  #-------------------------------------------------------------------------
  # ROUTES 
  #------------------------------------------------------------------------

  
  # get actors -----------------------------------------
  @app.route('/actors' )
  def get_actors():

      
      actors= Actors.query.all()   #query.order_by(Actors.id).all()
      page=request.args.get('page', 1, type=int)
      start=(page -1) * PER_PAGE
      end= start + PER_PAGE
      current_actors= [actor.format() for actor in actors]
      current_actors=current_actors[start:end]

      if len(current_actors) ==0 :
          abort(404)

      
      return jsonify({"success": True,
                      "actors": current_actors
                      })

  # get movies -------------------------------------------------
  @app.route('/movies')
  def get_movies():
      movies=Movies.query.all() #query.order_by(Movies.id).all()
      page=request.args.get('page', 1, type=int)
      start=(page -1) * PER_PAGE
      end= start + PER_PAGE
      current_movies=[movie.format() for movie in movies]
      current_movies=current_movies[start:end]

      if len(current_movies)==0:
           abort(404)
      return jsonify({"success": True,
                       "movies": current_movies
                       })
  
  # DELETE -------------------------------------------------------------------------------------------------
  # delete actors by id
  @app.route('/actors/<id>', methods=['DELETE'] )
  @requires_auth('delete:actor_movie')
  def delete_actor(payload ,id):
      actor= Actors.query.filter(Actors.id==id).one_or_none()
      
      if not actor:
        abort(404)

      try:
        actor.delete_from_db()
        return jsonify({ "success": True,
                        "deleted": actor.id})

      except:
          abort(400)

  # delete movie by id ---------------------------------------------
  @app.route('/movies/<id>', methods=['DELETE'] )
  @requires_auth('delete:actor_movie')
  def delete_movie(payload ,id):
      movie= Movies.query.filter(Movies.id==id).one_or_none()

      if not movie:
        abort(404)

      try:
        movie.delete_from_db()
        return jsonify ({ "success": True,
                      "deleted": movie.id})

      except:
        abort(400)

  #POST -------------------------------------------------------------------------
  # create new actor
  @app.route('/actors', methods=['POST'])
  @requires_auth('post:actor_movie')
  def create_new_actors(payload):
      body = request.get_json()
      print("body")
      print(body)

      actor_name=body.get('name')
      actor_date_of_birth=body.get('date_of_birth')
      actor_gender=body.get('gender')
      
      try:
          actor=Actors(name=actor_name, date_of_birth=actor_date_of_birth , gender=actor_gender)
          actor.save_to_db()

          return jsonify ({"success": True,
                       "actor": actor.id
                     })
      except:
        abort(422)

  # create new movie
  @app.route('/movies', methods=['POST'])
  @requires_auth('post:actor_movie')
  def create_new_movie(payload):
      body = request.get_json()
      print(body)

      title=body.get('title')
      release_date=body.get('release_date')
      
      try:
          movie=Movies(title=title , release_date=release_date)
          movie.save_to_db()

          return jsonify ({'success': True,
                          'new_movie': movie.id
                      })
      except:
           abort(422)

           
  # edit using PATCH method ------------------------------------------------------------------------
  # edit actor by id 
  @app.route('/actors/<id>' , methods=['PATCH'] )
  @requires_auth('patch_actor_movie')
  def edit_actor(payload ,id):
      body =request.get_json() 

      actor=Actors.query.filter(Actors.id==id).one_or_none()
      if not actor:
          abort(404)

      try:
          
          if 'name' in body:
            actor.name=body.get('name')
          if 'date_of_birth' in body:
            actor.date_of_birth=body.get('date_of_birth')
          if 'gender' in body:
            actor.gender=body.get('gender')
            
          if 'name' is None and 'date_of_birth' is None and 'gender' is None :
            abort (400)
          actor.update()
      
          return jsonify ({"success": True,
                        "actor":actor.id
                      })
      except:
          abort(400)
  
  # eait movie by id
  @app.route('/movies/<id>' , methods=['PATCH'])
  @requires_auth('patch_actor_movie')
  def edit_movie(payload ,id):
      body =request.get_json() 

      movie=Movies.query.filter(Movies.id==id).one_or_none()
      if not movie:
          abort(404)
      try:
           
          if 'title' in body:
            movie.title=body.get('title')
          if 'release date' in body:
            movie.release_date=body.get('release_date')

          if 'title' is None and 'release date' is None :
            abort (400)
            
          movie.update()
      
          return jsonify({"success": True,
                        "movie":movie.id
                      })
      except:
          abort(400)


  ########################################################################################################
  # Error Handling

  @app.errorhandler(422)
  def unprocessable(error):
    return jsonify({
        "success": False,
        "error": 422,
        "message": "unprocessable"
    }), 422

  @app.errorhandler(404)
  def not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "resource not found"
        }), 404

  @app.errorhandler(400)
  def Bad_Request(error):
      return jsonify({
      "success": False, 
      "error": 400,
      "message": " Bad Request ,The server could not understand the request due to invalid syntax"
      }), 400


  @app.errorhandler(405)
  def method_not_allowed(error):
      return jsonify({
      "success": False, 
      "error": 405,
      "message": " method not allowed "
      }), 405




  return app

app = create_app()




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)