import re

TITLE_XPATH = '''//title/text()'''


def parse_zillow_details(zillow_dom_tree):
    address = zillow_dom_tree.xpath(TITLE_XPATH)
    if len(address) == 0:
        address = ''
    else:
        address = address[0]
        address = address.strip(' | Zillow')
        street_address = address.split(',')[0].strip(', ')
        city = address.split(',')[1].strip(', ')
        state = address.split(',')[2].split(' ')[1].strip(', ')
        zipcode = address.split(',')[2].split(' ')[2].strip(', ')

    data = {
        'address': address,
        'street_address': street_address,
        'city': city,
        'state': state,
        'zipcode': zipcode
    }
    return data
