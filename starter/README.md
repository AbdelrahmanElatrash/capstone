# capstone

# Full Stack capstoe project
# Backend - Full Stack capstoe project
this project working in backend 
### Installing Dependencies for the Backend

1. **Python 3.7** - it is recommended to install the following version of python to run the project without errors [python3.7.9](https://www.python.org/downloads/release/python-379/)

if you have an another version like 3.9 or higher do the following 
>>python --version   // to get your python version
output >> 3.9.2
>>>
    1. uninstall old python version 
    2. install python 3.7.9 don't forget to check the add to path while installing
    3. after you install make sure that when typeing python -v  in the termainal it gives you python3.7.9
    4. if the above gives you old python version restart the shell and make sure you uninstalled 3.9


2. **Virtual Enviornment** - We recommend working within a virtual environment whenever using Python for projects.

>>python3 -m venv muenv
>> source ./env/bin/activate    // to activate your envirornmint
3. **PIP Dependencies** - Once you have your virtual environment setup and running, install dependencies by naviging to 
`/starter`
>> pip3 install -r requirements.txt

This will install all of the required packages we selected within the `requirements.txt` file.


### Database Setup
>>source ./setup.sh
check your database name ,postgres user and pass 



### Running the server locally
To run the server, execute:
* linux bash
> export FLASK_APP=flaskr
> export FLASK_DEBUG=1
> flask run --reload

* windows terminal
> set FLASK_APP=flaskr
> se FLASK_DEBUG=development
> flask run 


## deploiment
this project working and deploied in herocu
https://myapp-663697222.herokuapp.com/


## authentication
API permissions:
    'patch_actor_movie'
    'post:actor_movie'
    'delete:actor_movie'

api roles for:
   employee : 'post:actor_movie'
   owner_token: have all permissions

acsses token
    owner_token="eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkVnQ2k3SHl6YmdROHdBNl9pXzBDYiJ9.eyJpc3MiOiJodHRwczovL2RldmVsb3BtZW50MTcwLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MWVjYzRkOTU5ZTBhOTAwNzFkOTI1NTUiLCJhdWQiOiJteWFwaSIsImlhdCI6MTY0Nzc4MDEyMCwiZXhwIjoxNjQ3ODY2MTIwLCJhenAiOiJXZnFJMDN1b29VTkk3aXA2blZaa1FHanlIVkpyR3JKdCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9yX21vdmllIiwicGF0Y2hfYWN0b3JfbW92aWUiLCJwb3N0OmFjdG9yX21vdmllIl19.IaY_UnVNFVgcvPCM4ylQY03V7eL3acfsXdavej834j7kLZhbmW6UdP7xXpJmetgD6HyM7tKCUjxAZssK4VW1oM8SpHsneNeLfsLFhxzDKSw9gqT9A9foI36neSE3fg-4YzOWQ0kmHDFjMgZw5xrELUH4ZmyU-9tewdk56KRMEwle0xGza8XLOhJV6mB-BTyi-ccy5ozpoFPF8ZclSylLhGoWjqvGXjdU9wqXyx1y2xsKZCMuJx4lDxXo5k_aMF84b-ARIFPrya5Q6fAg_1ZP2J1IKczwOCVYcH7ihLeawx1JiUH50BQxaMHbvL5J2zqdBbfeDF9ixWxYVu-4_n7GAw

    employee_token="eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkVnQ2k3SHl6YmdROHdBNl9pXzBDYiJ9.eyJpc3MiOiJodHRwczovL2RldmVsb3BtZW50MTcwLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MWY2YmE4NGJkNDk0ZTAwNzA2NTlhNTMiLCJhdWQiOiJteWFwaSIsImlhdCI6MTY0Nzc4MDIxNSwiZXhwIjoxNjQ3ODY2MjE1LCJhenAiOiJXZnFJMDN1b29VTkk3aXA2blZaa1FHanlIVkpyR3JKdCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsicG9zdDphY3Rvcl9tb3ZpZSJdfQ.WkiYVGCAJarz1HGEo_72bPetNEWCgqz_eoRLWN-AcyFuMr0N5N7l6Et_Hq8LqNJiCIxC1AO-PPKHmQbmAEHMQtys4TNSbKDc4VRrmzFBH-0wDgAGTalVFJJeqMnwYJlgthnm1cn4uO4QrMSuWJ9jNujqd7m1Xtyqi6jZ7STErLecMAMG0F9MIiJc5Iw8R9Fq7IlwB_N9w0nF5KrmExhzNqRzTXrbhugWmGyiVG9c-3qq_h3fXQnmvi19rMWhu95jqGwpClsb1zKtR6_wEQCts0DWDujO8OEwqg01M1HrWgXggvauucGnUk0y956qaJApajUik0JkiQYcs3SdGX6gZw"


## end point

this is the repository for the example movies and actors 
included in the repo the tokens for the different 2 users you will find them in the test_app.py


GET "/actors"  //public end point

Fetches an json that contains an array of actors
Request Arguments: None
Query Arguments: -page = the page number -limit = number of items per page
Request Body: None
Returns:
an array of actors as show in the example response
status: 200
Example Response:
         "actors": [
        {
            "date_of_birth": "Wed, 01 Jan 2014 00:00:00 GMT",
            "gender": "male",
            "id": 2,
            "name": "Leonardo Wilhelm DiCaprio"
        },

GET "/movies"  //public end point
Fetches an json that contains an array of movies
Request Arguments: None
Query Arguments: -page = the page number -limit = number of items per page
Request Body: None
Returns:
an array of movies as show in the example response
status: 200
Example Response:
         "movies": [
        {
            "id": 1,
            "release date": "1997-12-17",
            "title": "titanic"
        },

POST "/actors"  // requires_auth('post:actor_movie')
POST "/movies"  // requires_auth('post:actor_movie')
Fetches an json that contains an array of movie_id or actor_id with success
Request Arguments: authorization headers contains  bearer token
Request Body: json
for movie : { 
           "title":"titanic",
           "release date":"1997-12-17"
           }

for actors: {
            "name":"Leonardo Wilhelm DiCaprio",
            "date_of_birth":"1974-11-11",
            "gender":"male"
            }

Returns:
 An object with a single key, new movie or new actor

movie: {
    "new_movie": 8,
    "success": true
    }   

actor: {
    "actor": 18,
    "success": true
    }  


DELETE "/actors/${id}" //requires_auth('delete:actor_movie')
DELETE "/movies/${id}" //requires_auth('delete:actor_movie')

delete actor/movie using an ID , the actor/movie will be removed.
Request Arguments: id {int} and authorization headers contains  bearer token
Request Body: None
return 
       {"deleted": actor.id}

PATCH "actors/${id}"  // requires_auth('patch_actor_movie')
PATCH "movies/${id}"  // requires_auth('patch_actor_movie')
patch actor/movie using an ID , the actor/movie will be update
Request Arguments: id {int} and authorization headers contains  bearer token
you can update one or more attribute
Request Body: json obj
   for actor : {
               "date_of_birth":"1974-11-11"
              }
   for movie :{
             "title":"titanic2",
              "release_date":"2010-08-07"
             }

return :
       {
       "actor": 9,
       "success": true
        }