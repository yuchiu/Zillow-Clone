
from dotenv import load_dotenv  # pylint: disable=E0401
from os.path import join, dirname
import os
import time
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), './', 'config'))

import mongodb_client  # pylint: disable=E0401
from cloudAMQP_client import CloudAMQPClient  # pylint: disable=E0401

dotenv_path = join(os.path.dirname(__file__), '..', '.env')
load_dotenv(dotenv_path)

MQ_REAL_ESTATE_FETCH_TASK_URI = os.environ.get(
    "MQ_REAL_ESTATE_FETCH_TASK_URI")
MQ_REAL_ESTATE_FETCH_TASK_NAME = os.environ.get(
    "MQ_REAL_ESTATE_FETCH_TASK_NAME")


FETCH_SIMILIAR_PROPERTIES = False
PROPERTY_TABLE_NAME = 'property'

SCRAPER_SLEEP_SECONDS = 1

cloudAMQP_client = CloudAMQPClient(
    MQ_REAL_ESTATE_FETCH_TASK_URI, MQ_REAL_ESTATE_FETCH_TASK_NAME)


def handle_message(msg):
    pass


while True:
    if cloudAMQP_client is not None:
        msg = cloudAMQP_client.getMessage()
        if msg is not None:
            handle_message(msg)
        time.sleep(SCRAPER_SLEEP_SECONDS)
