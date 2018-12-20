from pymongo import MongoClient  # pylint: disable=E0401

import os
import sys
from os.path import join, dirname
from dotenv import load_dotenv  # pylint: disable=E0401

dotenv_path = join(os.path.dirname(__file__), '..', '..', '.env')
load_dotenv(dotenv_path)

SERVICE_REAL_ESTATE_DB_MONGO_HOST = os.environ.get(
    "SERVICE_REAL_ESTATE_DB_MONGO_HOST")
SERVICE_REAL_ESTATE_DB_MONGO_PORT = os.environ.get(
    "SERVICE_REAL_ESTATE_DB_MONGO_PORT")
SERVICE_REAL_ESTATE_DB_MONGO_NAME = os.environ.get(
    "SERVICE_REAL_ESTATE_DB_MONGO_NAME")
SERVICE_REAL_ESTATE_DB_MONGO_USER = os.environ.get(
    "SERVICE_REAL_ESTATE_DB_MONGO_USER")
SERVICE_REAL_ESTATE_DB_MONGO_PASS = os.environ.get(
    "SERVICE_REAL_ESTATE_DB_MONGO_PASS")

# instance
client = MongoClient("%s:%s" %
                     (SERVICE_REAL_ESTATE_DB_MONGO_HOST, int(SERVICE_REAL_ESTATE_DB_MONGO_PORT)))


def get_db(db=SERVICE_REAL_ESTATE_DB_MONGO_NAME):
    db = client[db]
    db.authenticate(SERVICE_REAL_ESTATE_DB_MONGO_USER,
                    SERVICE_REAL_ESTATE_DB_MONGO_PASS)
    return db
