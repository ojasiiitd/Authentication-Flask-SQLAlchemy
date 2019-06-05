# Authentication-Flask-SQLAlchemy

A basic flask application which implements a simple **User authentication framework** with *Login*, *SignUp* and *Logout* options. **Databaseing has been done using Flask-SQLAlchemy module, which uses SQLite**.

A simple website using [Bulma](https://bulma.io/ "Bulma Website") has been used for styling *(no external CSS used !)*. Login and SignUp forms have been made using *WTForms*.

## Instructions to Setup :

* Fork this repo.
* Use `git clone https://github.com/<your-github-username>/Authentication-Flask-SQLAlchemy.git` to clone this repo into your system
* Install pip3 on your system by `sudo apt-get install python3-pip` if not already installed.
* Create a virtual environment by the name of **venv**. Information in setting up virtualenv can be found [here](https://docs.python-guide.org/dev/virtualenvs/ "Pipenv & Virtual Environments").
* Enter your virtualenv by `source venv/bin/activate`
* Do a `pip install -r requirements.txt` to install the required packages.
* All the databasing has been carried out using SQLite, which is pre-installed with Python. A guite to basic SQLite commands can be found [here](https://www.tutorialspoint.com/sqlite/ "Basic SQLite")
* For info on the commands Flask-SQLAlchemy uses to interact with SQLite, [click here](https://flask-sqlalchemy.palletsprojects.com/en/2.x/ "Flask-SQLAlchemy Deocumentation")

## Working :

* Open command line and enter your virtualenv venv.
* Use `python run.py` and go to `localhost:5000` to show the webpage.