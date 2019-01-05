
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import zillow_web_scraper_client  # pylint: disable=E0401

print(zillow_web_scraper_client.get_property_by_zpid(30695213))
