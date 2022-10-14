# ku-polls
[![Python application](https://github.com/premepreme/ku-polls/actions/workflows/python-package.yml/badge.svg)](https://github.com/premepreme/ku-polls/actions/workflows/python-package.yml)
[![codecov](https://codecov.io/gh/premepreme/ku-polls/branch/main/graph/badge.svg?token=ROXD815LEK)](https://codecov.io/gh/premepreme/ku-polls)

An application for conducting a poll or survey, written in Python using Django. It is based on the [Django Tutorial project](https://docs.djangoproject.com/en/4.1/intro/tutorial01/), with additional functionality.

This application is part of the [Individual Software Process course](https://cpske.github.io/ISP/)at [Kasetsart University](https://www.ku.ac.th/th).

# Install and Run
1. Clone this project repository to your machine.
```
git clone https://github.com/premepreme/ku-polls.git
```
2. Get into the directory of this repository.
```
cd ku-polls
```
3. Create a virtual environment.
```
python -m venv venv
```
4. Activate the virtual environment.
```
. env/bin/activate
```
5. Install all required packages.
```pip install -r requirements.txt```
Create .env file in ku-polls
```
SECRET_KEY = 'django-insecure-)u=f_#17(&3%@q&1w@3c6f!^8ctf59(id3g2)%mkz*2b6-&$00'
DEBUG = True
TIME_ZONE = UTC
```
6. Run this command to migrate the database and load the data.
```
python manage.py migrate
python manage.py loaddate data/*.json
```
7. Start running the server by this command.
```
python manage.py runserver
   ```


# [Project Documents](https://github.com/premepreme/ku-polls/wiki)

* [Task board](https://github.com/users/premepreme/projects/1)
* [Vision statement](https://github.com/premepreme/ku-polls/wiki/Vision-Statement)
* [Requirements](https://github.com/premepreme/ku-polls/wiki/Requirements)
* [Development Plan](https://github.com/premepreme/ku-polls/wiki/Development-Plan)
* [Iteration 1 plan](https://github.com/premepreme/ku-polls/wiki/Iteration-1-Plan) | [Iteration 1 broad](https://github.com/users/premepreme/projects/1/views/2) 
* [Iteration 2 plan](https://github.com/premepreme/ku-polls/wiki/Iteration-2-Plan) | [Iteration 2 broad](https://github.com/users/premepreme/projects/1/views/3) 
* [Iteration 3 plan](https://github.com/premepreme/ku-polls/wiki/Iteration-3-Plan) | [Iteration 3 broad](https://github.com/users/premepreme/projects/1/views/5) 
* [Iteration 4 plan](https://github.com/premepreme/ku-polls/wiki/Iteration-4-Plan) | [iteration 4 broad](https://github.com/users/premepreme/projects/1/views/6?layout=board)


# Demo users


| Username   | Password |
|------------|----------|
| username1  | password |
| username2  | password |
| username3  | password |
| username4  | password |

