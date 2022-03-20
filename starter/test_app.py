
import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from models import setup_db , Movies, Actors


employee_token="eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkVnQ2k3SHl6YmdROHdBNl9pXzBDYiJ9.eyJpc3MiOiJodHRwczovL2RldmVsb3BtZW50MTcwLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MWY2YmE4NGJkNDk0ZTAwNzA2NTlhNTMiLCJhdWQiOiJteWFwaSIsImlhdCI6MTY0NzcyNjA4NCwiZXhwIjoxNjQ3ODEyMDg0LCJhenAiOiJXZnFJMDN1b29VTkk3aXA2blZaa1FHanlIVkpyR3JKdCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsicG9zdDphY3Rvcl9tb3ZpZSJdfQ.p6xxKbFkqgaBxzTMgiSjDkZKdkUc71rzWSb3qgXJvrKqJtfl7aXcMZ5RjjpVzNlYtQGA36MjS1FG-CZ0ulHt4VDSX2qxNoyRNc2vHg9Ck5kSjSPKU9H6k3nnkgJPdw8XkCt7e9IFT0oaMeqTFcWcIzUb5IBZIjm0Z_c_AxmbtqvoTaMmwRCbv_auagHWB__bUCJzYQ72QRxZP10F6RufgMa1Atjw_62WxJUbOPO-I6l8L7mT7woLZyr3xv590VprI0VB9a1p_X-ZCqoh7nmOuSZGpdFHbRo19Sd3KScp8mRFP73d1IECVYc_9GcH6JJku4G8_2fKe1D3Un7dav_MAA"
owner_token="eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkVnQ2k3SHl6YmdROHdBNl9pXzBDYiJ9.eyJpc3MiOiJodHRwczovL2RldmVsb3BtZW50MTcwLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MWVjYzRkOTU5ZTBhOTAwNzFkOTI1NTUiLCJhdWQiOiJteWFwaSIsImlhdCI6MTY0NzcyNTk2MiwiZXhwIjoxNjQ3ODExOTYyLCJhenAiOiJXZnFJMDN1b29VTkk3aXA2blZaa1FHanlIVkpyR3JKdCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9yX21vdmllIiwicGF0Y2hfYWN0b3JfbW92aWUiLCJwb3N0OmFjdG9yX21vdmllIl19.jJ4Ednh0Nv42mXZ1n14VzKszjO0ig_gKtaUKp8FZx70OCco7RnWuoW0N_7_LLiSmJXfIqEt6S6IDcNuDV56i8xQrMq0joNhMq5PimQjrRVLFKAZJI3yfCSU7Z3XuzMoAqnyU92DIlhyyQ9NjPcCx6ipyffiG6Zm4jsHDVqKXsD2VVdCmz6A9dv1VwQ7FlBsEdkcAr_I0H2p3lLjznjYz1KJ9vFbSi5ZwXUqcxXG8tuQ7y9gm54nPd-iSsne9nkZ2YPmN4fpBoFbXMxwB799bQpJ1yFRFZE-i7ypqXXYJjrvxWQWUeGwfHau4PLfWBYT4qS0U9OenUGGgIK-vJueXeg"
fake_token="eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkVnQ2k3SHl6YmdROHdBNl9pXzBDYiJ9.eyJpc3MiOiJodHRwczovL2RldmVsb3BtZW50MTcwLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MWVjYzRkOTU5ZTBhOTAwNzFkOTI1NTUiLCJhdWQiOiJteWFwaSIsImlhdCI6MTY0NzYyOTc3MiwiZXhwIjoxNjQ3NzE1NzcyLCJhenAiOiJXZnFJMDN1b29VTkk3aXA2blZaa1FHanlIVkpyR3JKdCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9yX21vdmllIiwicGF0Y2hfYWN0b3JdsfdsfdsfsfffbW92aWUiLCJwb3N0OmFjdG9yX21vdmllIl19.BlShWXwxb5Ab6E-YpeG5RDZP7if9ph-D5JgeUANJfJSJ7pPDsJM8GO08cozpSjpWMiN9AU137KemTc07Xkr1bprbhjfP-bvEtdGtW0Bu5M3rdbqGLRpZVxvC7r2dnNPw_GJjM98vnIX105duSjJTGI0VIpL9q6lGskoi1tyoXWLsX1fbqsdSXX_epwPdfbaBjDBYkPmNw7wFxQU9sTg5NImsjL9AOyM2BhAR4kt-kSuxX4xIp9fgfhfghgfhgfhfhfghgdReFhhHVXaDGuAlKd1Byc6HuAkqdENyMFlxEbyH3jUwFzoFYKCwrQ3ryFLw"
expired_token="eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkVnQ2k3SHl6YmdROHdBNl9pXzBDYiJ9.eyJpc3MiOiJodHRwczovL2RldmVsb3BtZW50MTcwLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MWVjYzRkOTU5ZTBhOTAwNzFkOTI1NTUiLCJhdWQiOiJteWFwaSIsImlhdCI6MTY0NzYyOTc3MiwiZXhwIjoxNjQ3NzE1NzcyLCJhenAiOiJXZnFJMDN1b29VTkk3aXA2blZaa1FHanlIVkpyR3JKdCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9yX21vdmllIiwicGF0Y2hfYWN0b3JfbW92aWUiLCJwb3N0OmFjdG9yX21vdmllIl19.BlShWXwxb5Ab6E-YpeG5RDZP7if9ph-D5JgeUANJfJSJ7pPDsJM8GO08cozpSjpWMiN9AU137KemTc07Xkr1bprbhjfP-bvEtdGtW0Bu5M3rdbqGLRpZVxvC7r2dnNPw_GJjM98vnIX105duSjJTGI0VIpL9q6lGskoi1tyoXWLsX1fbqsdSXX_epwPdfbaBjDBYkPmNw7wFxQU9sTg5NImsjL9AOyM2BhAR4kt-kSuxX4xIp9PuPhCOBqg6KC2p6RtUGmvTuHYprYQLYgB47GeE3bYIReFhhHVXaDGuAlKd1Byc6HuAkqdENyMFlxEbyH3jUwFzoFYKCwrQ3ryFLw"



database_path="postgresql://postgres:00134256@localhost:5432/test_casting"#os.environ['DATABASE_URL']
class appTestCase(unittest.TestCase):
     
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client

        self.database_path = database_path
        setup_db(self.app, self.database_path)

        self.new_movie= { 
                        "title":"titanic",
                        "release date":"1997-12-17"
                        }

        self.new_actor={'name':'Leonardo Wilhelm DiCaprio',
                       'date_of_birth':'1974-11-11',
                        'gender':'male'}

        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

    def tearDown(self):
        """Executed after reach test"""
        pass

    # test get movies  --------------------------[ GET ] ---------------------------
    def test_1_get_movies(self):
        response = self.client().get('/movies')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)

    # test get actors
    def test_2_get_actors(self):
        response = self.client().get('/actors')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)

    # test get movies with a wrong page parameter
    def test_3_get_movies_404(self):
        response = self.client().get('/movies?page=2000')
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['success'], False)

    # test get actors with a wrong page parameter
    def test_4_get_actors_404(self):
        response = self.client().get('/actors?page=2000')
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['success'], False)

    # test delete a movie with id exists id -----------------[ DELETE ]-------------------------------
    def test_5_delete_movie(self):

        headers = {'Authorization': 'Bearer {}'.format(owner_token)}

        response = self.client().delete('/movies/1',headers=headers)
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted'],1)

    # test delete a actor with id exists id
    def test_6_delete_actor(self):

        headers = {'Authorization': 'Bearer {}'.format(owner_token)}

        response = self.client().delete('/actors/1',headers=headers)
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted'],1)

    # test detele a actors with a id that is not in the database
    def test_7__delete_actors_404(self):
        headers = {'Authorization': 'Bearer {}'.format(owner_token)}
        response = self.client().delete('/actors/200',headers=headers )
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['success'], False)

    
    
    # test delet not permission
    def test_8_delet_actors_403(self):
        headers = {'Authorization': 'Bearer {}'.format(employee_token)}
        response = self.client().delete('/actors/5',headers=headers)
        #data = json.loads(response.data)
        #print(data)
        self.assertEqual(response.status_code, 403)


    # test create new movie -----------------------[ CREATE ] -------------------------
    def test_9_create_movie(self):
        headers = {'Authorization': 'Bearer {}'.format(owner_token)}
        response = self.client().post('/movies',headers=headers, json=self.new_movie)

        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        
        self.assertEqual(data['success'], True)

    # creation not allowed
    def test_10_movies_creation_not_allowed_405(self):
        headers = {'Authorization': 'Bearer {}'.format(owner_token)}
        response = self.client().post('/movies/1',headers=headers ,json=self.new_movie)
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 405)
        self.assertEqual(data['success'], False)

    # test create new actor
    def test_11_create_new_actor(self):
        headers = {'Authorization': 'Bearer {}'.format(employee_token)}
        response = self.client().post('/actors',headers=headers, json=self.new_actor)

        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)

    # test create without authorize
    def test_12_create_new_movie(self):
        headers = {'Authorization': 'Bearer {}'.format(None)}
        response = self.client().post('/actors',headers=headers, json=self.new_movie)

        #data = json.loads(response.data)
        
        self.assertEqual(response.status_code, 401)
        #self.assertEqual(data['success'], False)


    # test edit movie ------------------------[ EDIT ]--------------------------------------
    def test_13_edit_movie(self):
        headers = {'Authorization': 'Bearer {}'.format(owner_token)}
        response = self.client().patch('/movies/3',headers=headers,json={"title":"unknown"})

        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
 
    # test edit actor
    def test_14_edit_movie(self):
        headers = {'Authorization': 'Bearer {}'.format(owner_token)}
        response = self.client().patch('/actors/3',headers=headers,json={"name":"unknown"})

        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
 

    # test edit with fake token
    def test_15_edit_movie(self):
        headers = {'Authorization': 'Bearer {}'.format(fake_token)}
        response = self.client().patch('/movies/1',headers=headers,json={"title":"unknown"})

        #data = json.loads(response.data)

        self.assertEqual(response.status_code, 401)
        
 

    # test edit with expire token
    def test_16_edit_actor(self):
        headers = {'Authorization': 'Bearer {}'.format(expired_token)}
        response = self.client().patch('/actors/1',headers=headers,json={"name":"unknown"})

        #data = json.loads(response.data)

        self.assertEqual(response.status_code, 401)
        
    # test_400_for_failed_edit
    def test_17_failed_edit_movie(self):
        headers = {'Authorization': 'Bearer {}'.format(owner_token)}
        response = self.client().patch('/movies/4',headers=headers)

        data = json.loads(response.data)

        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['success'], False)
 
