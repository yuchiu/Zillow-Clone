import requests
import os
import sys
import random
from lxml import html
from zillow_parser import parse_zillow_details  # pylint: disable=E0401
import user_agents  # pylint: disable=E0401


URL = "http://www.zillow.com"
GET_ZPID_PATH = "homes"


def build_url(url, path):
    if url[-1] == '/':
        url = url[:-1]
    return '%s/%s' % (url, path)


""" get property information by zillow property id (zpid)"""


def get_property_by_zpid(zpid):
    request_url = '%s/%s_zpid' % (build_url(URL, GET_ZPID_PATH), str(zpid))
    session_requests = requests.session()
    response = session_requests.get(
        request_url, headers=user_agents.get_headers())
    print(response)

    tree = html.fromstring(response.content)
    data = parse_zillow_details(tree)

    print(data)
    return data


""" get similiar property for sale"""


def get_similiar_properties_for_sale_by_id(zpid):
    return {}
