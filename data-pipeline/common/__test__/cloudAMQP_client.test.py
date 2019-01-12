
import os
import sys
from dotenv import load_dotenv  # pylint: disable=E0401
from os.path import join, dirname
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from cloudAMQP_client import CloudAMQPClient  # pylint: disable=E0401

dotenv_path = join(os.path.dirname(__file__), '..', '..', '..', '.env')
load_dotenv(dotenv_path)

MQ_REAL_ESTATE_FETCH_TASK_URI = os.environ.get(
    "MQ_REAL_ESTATE_FETCH_TASK_URI")
MQ_REAL_ESTATE_FETCH_TASK_NAME = os.environ.get(
    "MQ_REAL_ESTATE_FETCH_TASK_NAME")

client = CloudAMQPClient(
    MQ_REAL_ESTATE_FETCH_TASK_URI, MQ_REAL_ESTATE_FETCH_TASK_NAME)


client.sendMessage({'zpid': '30691509'})
