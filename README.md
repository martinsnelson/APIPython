BUILD
docker-compose -f docker-compose.yml up --build

docker-compose down

pip install virtualenv
virtualenv venv
ctrl + shift + p
na janela buscar  python interpreter
pip install flask
pip install flask_cors

python app.py

pip freeze > requirements.txt

################################################
Path: PythonAPI/api
como rodar esse projeto app
no command    bash
export FLASK_APP=app
export FLASK_ENV=Development
export FLASK_DEBUG=True
flask run


flask db
flask db init
flask db migrate
flask db upgrade
flask routes

pipenv install flask-sqlalchemy
pipenv install flask-migrate
pipenv install flask-marshmallow
pipenv install marshmallow-sqlalchemy
pipenv install -d requests ipdb
################################################

flask==1.0.2
flask-cors
flask_restful==0.3.6
flask_script
flask_sqlalchemy
flask_migrate
flask_marshmallow
marshmallow
marshmallow-sqlalchemy
psycopg2



…or create a new repository on the command line
echo "# tesrrrrr" >> README.md
git init
git add README.md
git commit -m "first commit"
git remote add origin https://github.com/martinsnelson/APIPython.git
git push -u origin master


…or push an existing repository from the command line
git remote add origin https://github.com/martinsnelson/APIPython.git
git push -u origin master


…or import code from another repository
You can initialize this repository with code from a Subversion, Mercurial, or TFS project.