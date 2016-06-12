import os

basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE = "tasker.db"
DB_REPO = "database_repo"

SECRET_KEY = "O6QSW3!67G13y6{4i|-KB2h8#|o-Q*"
DATABASE_PATH = os.path.join(basedir, DATABASE)

SQLALCHEMY_DATABASE_URI = "sqlite:///" + DATABASE_PATH
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, DB_REPO)
 