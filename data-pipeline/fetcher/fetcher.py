
from dotenv import load_dotenv  # pylint: disable=E0401
from os.path import join, dirname
import os
import time
import json
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))
import mongodb_client  # pylint: disable=E0401
import zillow_scraper  # pylint: disable=E0401
from cloudAMQP_client import CloudAMQPClient  # pylint: disable=E0401

dotenv_path = join(os.path.dirname(__file__), '..', '..', '.env')
load_dotenv(dotenv_path)

MQ_REAL_ESTATE_FETCH_TASK_URI = os.environ.get(
    "MQ_REAL_ESTATE_FETCH_TASK_URI")
MQ_REAL_ESTATE_FETCH_TASK_NAME = os.environ.get(
    "MQ_REAL_ESTATE_FETCH_TASK_NAME")

# 1 week
STALE_TIME = 3600 * 24 * 7

FETCH_SIMILIAR_PROPERTIES = True
PROPERTY_TABLE_NAME = 'property'

SCRAPER_SLEEP_SECONDS = 1

cloudAMQP_client = CloudAMQPClient(
    MQ_REAL_ESTATE_FETCH_TASK_URI, MQ_REAL_ESTATE_FETCH_TASK_NAME)


def handle_message(msg):
    print("dasdasddsaasdasdsd")
    task = json.loads(msg)

    zpid = task['zpid']
    # Scrape zillow for details
    property_detail = zillow_scraper.get_property_by_zpid(zpid)

    # update database
    db = mongodb_client.get_db()
    db[PROPERTY_TABLE_NAME].replace_one(
        {'zpid': zpid}, property_detail, upsert=True)

    if FETCH_SIMILIAR_PROPERTIES:
        # get its similiar property's zpid
        similiar_zpids = zillow_scraper.get_similiar_properties_for_sale_by_id(
            zpid)

        # generate tasks for similar zpids
        for zpid in similiar_zpids:
            # check if zpid is already scraped in our database
            # if it is already scraped, check if the data has passed our stale period
            # if it has passed the staled period, scrape the fresh data
            old = db[PROPERTY_TABLE_NAME].find_one({'zpid': zpid})
            if(old is not None and time.time() - old['last_update'] > STALE_TIME):
                continue
            cloudAMQP_client.sendMessage({'zpid': zpid})


while True:
    if cloudAMQP_client is not None:
        msg = cloudAMQP_client.getMessage()
        if msg is not None:
            handle_message(msg)
        time.sleep(SCRAPER_SLEEP_SECONDS)
