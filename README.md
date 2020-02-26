LearnWorld is app which enables children to learn and pronounce concepts in Hindi and English
# LearnWorld Capstone

The LearnWorld API is app which enables children to learn and pronounce concepts in Hindi and English.
This api is responsible for showing lessons and associated cards for learning. Also checks permissions and provides CRUD capabilities for Lesson and Card Models.
## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the root directory of this project and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

After installing the dependencies, execute the bash file `setup.sh` to set the user jwts, auth0 credentials and the remote database url by naviging to the root directory of this project and running:

```bash
source setup.sh
```

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server.

- [jose](https://python-jose.readthedocs.io/en/latest/) JavaScript Object Signing and Encryption for JWTs. Useful for encoding, decoding, and verifying JWTS.

## Running the server

From within the root directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
```

Setting the `FLASK_ENV` variable to `development` will detect file changes and restart the server automatically.

Setting the `FLASK_APP` variable to `app.py` directs flask to use the `app.py` file to find the application. 

## API Reference

#### GET '/', '/index'
  - Fetches a list of lessons
  - Request Arguments: None
  - Returns: A list of lesson object that contains key value pairs for lesson id, lesson name,lesson image and lesson summary. 

```
[
   {
    "id": 1,
    "lesson_name":"Animals",
    "lesson_image":"lion.jpg",
    "lesson_summary":"Learn about animals"
   },
   {
    "id": 2,
    "lesson_name":"Fruits",
	"lesson_image":"watermelon.jpg",
	"lesson_summary":"Learn about fruits"
   }
 ]
```
#### GET '/admin'
  - Renders admin html page which provides button for login and Create, Edit and Delete buttons for Lesson and Card Data Model
  - Request Arguments: None
  - Returns: None 

```
```
#### GET '/cards/<int:lesson_id>'
  - Creates a list of all cards for given lesson id
  - Request Arguments: lesson id
  - Returns: A list of card object that contains key value pairs for card id, card name,card image english concept hindi concept and lesson id.  

```
[
   {
    "id": 1,
	"card_name":"Lion",
	"card_image":"lion.jpg",
	"english_concept":"lion",
	"hindi_concept":"शेर",
	"lesson_id":1
   },
   {
    "id": 2,
	"card_name":"Monkey",
	"card_image":"monkey.jpg",
	"english_concept":"monkey",
	"hindi_concept":"बंदर",
	"lesson_id":1
   }
 ]
```
#### GET '/lessons/create'
  - Renders new lesson creation form
  - Request Arguments: None
  - Returns: None 

#### POST "/lessons/create"
  - Adds a lesson to the database
  - Request Body:

      `lesson_name`: Lesson name    
      `lesson_image`: image name for the lesson from static image folder
      `lesson_summary`: Brief description about the lesson
```
{
    "id": 1,
    "lesson_name":"Animals",
    "lesson_image":"lion.jpg",
    "lesson_summary":"Learn about animals"
}
```
#### GET '/lessons/edit'
  - Redirects back to admin page which will ask for lesson id for editing
  - Request Arguments: None
  - Returns: None 

#### POST "/lessons/edit"
    - Collects data about lesson requested to be edited and sends to Edit Lesson Form
    - Request Body:

      `lesson_id`: Id of lesson user wantsto edit    
    - Return Lesson object for the requested lesson id  

```
{
    "id": 1,
    "lesson_name":"Animals",
    "lesson_image":"lion.jpg",
    "lesson_summary":"Learn about animals"
}
```
#### GET "/lessons/<int:lesson_id>/edit"
    - Collects data about lesson requested to be edited and sends to Edit Lesson Form
    - Request Body: None
    - Return Lesson object for the requested lesson id  

```
{
    "id": 1,
    "lesson_name":"Animals",
    "lesson_image":"lion.jpg",
    "lesson_summary":"Learn about animals"
}
```
#### POST(PATCH) "/lessons/<int:lesson_id>/edit"
  - Edits a lesson to the database
  - Request Body:
      `lesson_name`: Lesson name    
      `lesson_image`: image name for the lesson from static image folder
      `lesson_summary`: Brief description about the lesson
 ```
{
    "id": 1,
    "lesson_name":"Animals",
    "lesson_image":"lion.jpg",
    "lesson_summary":"Learn about animals"
}
```
#### POST(DELETE) "/lessons/delete"
  - Delete a lesson from the database
  - Request Body:
      `lesson_id`: Lesson id to be deleted    
  - Return: None
#### GET '/cards/create'
  - Renders new card creation form
  - Request Arguments: None
  - Returns: None 
  
#### POST "/cards/create"
  - Adds a lesson to the database
  - Request Body:

      `card_name`: Card Name    
      `card_image`: image name for the card from static image folder
      `english_concept`: English name for the card which will be prononced
	  `hindi_concept`: Hindi name for the card which will be prononced
      'lesson_id': Id of the lesson to which card belongs

```
{
   "id": 1,
   "card_name":"Lion",
   "card_image":"lion.jpg",
   "english_concept":"lion",
   "hindi_concept":"शेर",
   "lesson_id":1
}
```

#### GET '/cards/edit'
  - Redirects back to admin page which will ask for card id for editing
  - Request Arguments: None
  - Returns: None 
 
#### POST "/crads/edit"
    - Collects data about card requested to be edited and sends to Edit Card Form
    - Request Body:

      `card_id`: Id of lesson user wantsto edit    
    - Return Card object for the requested card id  

```
{
   "id": 1,
   "card_name":"Lion",
   "card_image":"lion.jpg",
   "english_concept":"lion",
   "hindi_concept":"शेर",
   "lesson_id":1
}
```

#### GET "/cards/<int:card_id>/edit"
    - Collects data about card requested to be edited and sends to Edit Card Form
    - Request Body: None
    - Return Card object for the requested card id  
```
{
   "id": 1,
   "card_name":"Lion",
   "card_image":"lion.jpg",
   "english_concept":"lion",
   "hindi_concept":"शेर",
   "lesson_id":1
}
```
#### POST(PATCH) "/cards/<int:card_id>/edit"
  - Edits a card to the database
  - Request Body:
      `card_name`: Card Name    
      `card_image`: image name for the card from static image folder
      `english_concept`: English name for the card which will be prononced
	  `hindi_concept`: Hindi name for the card which will be prononced
      'lesson_id': Id of the lesson to which card belongs
```
{
   "id": 1,
   "card_name":"Lion",
   "card_image":"lion.jpg",
   "english_concept":"lion",
   "hindi_concept":"शेर",
   "lesson_id":1
}
```

#### POST(DELETE) "/cards/delete"
  - Delete a card from the database
  - Request Body:
      `card_id`: Card id to be deleted    
  - Return: None

### Error Handling
We have two error handling routes, one for HTTPException and other for all generic Exceptions. Errors are returned as JSON objects in the following format:
```
{
    "success": False, 
    "error": 404,
    "message": "Resource not found."
}
```
## Testing

#### Testing remote server using postman

- Import the postman collection `./learnworld.postman_collection.json`.
  - This collection has 3 roles that have specific permissions detailed below.
  - Roles
    - Public
      - `get:lessons`,`get:cards`
    - Developer
      - `get:lessons`,`get:cards`,`post:lessons`,`post:cards`,`patch:lessons`,`patch:cards`
    - Admin (all permissions)
      - `get:lessons`,`get:cards`,`post:lessons`,`post:cards`,`patch:lessons`,`patch:cards`,`delete:lessons`,`delete:cards`
    
- Once imported, Run the collection and play around with the endpoints within folders `public`, `developer` and `admin`.

#### Running tests locally
To run the tests from ./test_app.py, first make sure you have ran and executed the setup.sh file to set the enviorment.

After setting the enviorment start your local postgress server:
```bash
pg_ctl -D /usr/local/var/postgres start
```

Then run the follwing commands to run the tests:
```
dropdb learnworld_test
createdb learnworld_test
psql learnworld_test < learnworld_test.psql
python test_app.py
```

