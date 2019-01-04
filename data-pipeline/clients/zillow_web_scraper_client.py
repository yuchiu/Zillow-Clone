

URL = "http://www.zillow.com"

GET_ZPID_PATH = "homes"


def build_url(url, path):
    if url[-1] == '/':
        url = url[:-1]
    return '%s/%s' % (url, path)


""" get property information by zillow property id (zpid)"""


def get_property_by_zpid(zpid):
    pass


""" get similiar property for sale"""


def get_similiar_properties_for_sale_by_id(zpid):
    pass
