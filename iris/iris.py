import os

from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

iris = Flask(__name__)

# Set enviornment variables from the database file
config_path = os.environ.get("CONFIG_PATH", "iris.config.DevelopmentConfig")
iris.config.from_object(config_path)

engine = create_engine(iris.config["DATABASE_URI"])
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()