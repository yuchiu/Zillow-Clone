import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import zillow_api  # pylint: disable=E0401

print (zillow_api.getSearchResults('65 Norfolk St UNIT 4', 'San Francisco, CA'))

print (zillow_api.getUpdatedPropertyDetails("15622377"))

print (zillow_api.getComps('15622377', 2))

print (zillow_api.getCompsZpids('15622377'))
