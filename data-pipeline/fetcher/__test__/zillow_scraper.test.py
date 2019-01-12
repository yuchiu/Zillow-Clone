
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import zillow_scraper  # pylint: disable=E0401

print(zillow_scraper.get_property_by_zpid(30691509))
