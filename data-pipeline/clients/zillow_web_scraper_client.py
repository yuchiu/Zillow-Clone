import requests
import os
import sys
import random
from lxml import html


""" setup user agent """
USER_AGENTS_FILE = os.path.join(
    os.path.dirname(__file__), 'user_agents.txt')
USER_AGENTS = []

with open(USER_AGENTS_FILE, 'r') as uaf:
    for ua in uaf.readlines():
        if ua:
            USER_AGENTS.append(ua.strip()[1:-1])

random.shuffle(USER_AGENTS)

URL = "http://www.zillow.com"
GET_ZPID_PATH = "homes"


def _get_headers():
    ua = random.choice(USER_AGENTS)
    headers = {
        "User-Agent": ua
    }
    return headers


def build_url(url, path):
    if url[-1] == '/':
        url = url[:-1]
    return '%s/%s' % (url, path)


""" get property information by zillow property id (zpid)"""


def get_property_by_zpid(zpid):
    request_url = '%s/%s_zpid' % (build_url(URL, GET_ZPID_PATH), str(zpid))
    session_requests = requests.session()
    response = session_requests.get(request_url, headers=_get_headers())
    print(response)

    try:
        tree = html.fromstring(response.content)
    except Exception:
        return {}

    address = tree.xpath('''//title/text()''')
    if len(address) == 0:
        address = ''
    else:
        address = address[0]
        address = address.strip(' | Zillow')
        street_address = address.split(',')[0].strip(', ')
        city = address.split(',')[1].strip(', ')
        state = address.split(',')[2].split(' ')[1].strip(', ')
        zipcode = address.split(',')[2].split(' ')[2].strip(', ')

    print(response.content)
    return {
        'zpid': zpid,
        'address': address,
        'street_address': street_address,
        'city': city,
        'state': state,
        'zipcode': zipcode
    }


""" get similiar property for sale"""


def get_similiar_properties_for_sale_by_id(zpid):
    pass
