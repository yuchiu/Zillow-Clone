import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', 'common'))
import user_agents  # pylint: disable=E0401
import requests  # pylint: disable=E0401
import random
import json
import time
from lxml import html
import re


SLEEP_TIME_IN_SECONDS = 1
# 2256
TEST_URL = "https://www.zillow.com/homes/for_sale/30693412_zpid/globalrelevanceex_sort/40.684088,-73.95155,40.578433,-74.089222_rect/12_zm/"

TEST_XPATH = '''//div[@id='list-results']/div[@id='search-results']/ul[@class='photo-cards']/li/article/@id'''

# TEST_XPATH = '''//*[@class="zsg-layout-bc-b"]'''


def run():
    session_requests = requests.session()
    response = session_requests.get(
        TEST_URL, headers=user_agents.get_headers())
    if response.status_code == 200:
        tree = html.fromstring(response.content)
        test = tree.xpath(TEST_XPATH)

        print('test')
        print(test)
        if(len(test) > 0):
            test = test[0]
        else:
            test = ''

        print('test')
        print(test)


if __name__ == '__main__':
    run()
