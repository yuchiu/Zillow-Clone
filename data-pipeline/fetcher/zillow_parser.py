import re
import json

TITLE_XPATH = '''//title/text()'''
IMAGE_XPATH = '''//img[@class="photo-tile-image"]/@src'''
DESCRIPTION_XPATH = '''//*[@class="zsg-content-item home-description"]/div[1]/div[1]/text()'''
PRICE_XPATH = '''//*[@class="price"]/span[@class="value"]/text()'''
BED_BATH_SIZE_XPATH = '''//*[@class="edit-facts-light"]/span/text()'''
TYPE_XPATH = '''//*[@class="home-facts-at-a-glance-section"]/div[1]/div[2]/div[2]/text()'''
LAT_LONG_XPATH = '''//*[@id="hdp-content"]/main/div[1]/div[1]/div[1]/script[2]/text()'''

SEARCH_XPATH_FOR_ZPID = '''//div[@id='list-results']/div[@id='search-results']/ul[@class='photo-cards']/li/article/@id'''
GET_INFO_XPATH_FOR_SALE = '''//div[@id='home-value-wrapper']/div[@class='estimates']/div/text()'''
GET_INFO_XPATH_FOR_FACTS = '''//div[@class='fact-group-container zsg-content-component top-facts']/ul/li/text()'''
GET_INFO_XPATH_FOR_ADDITIONAL_FACTS = '''//div[@class='fact-group-container zsg-content-component z-moreless-content hide']/ul/li/text()'''
GET_SIMILAR_HOMES_FOR_SALE_XPATH = '''//ol[@id='fscomps']/li/div[@class='zsg-media-img']/a/@href'''


def parse_zillow_details(zillow_dom_tree):
    '''address'''
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

    img_url = zillow_dom_tree.xpath(IMAGE_XPATH)
    if(len(img_url) > 0):
        img_url = img_url[0]
    else:
        img_url = ''

    '''description'''
    description = zillow_dom_tree.xpath(DESCRIPTION_XPATH)
    if(len(description) > 0):
        description = description[0]
    else:
        description = ''

    '''price'''
    price = zillow_dom_tree.xpath(PRICE_XPATH)
    if(len(price) > 0):
        price = price[0]
        price = re.sub("\D", "", price)
        price = int(price)
    else:
        price = ''

    '''bedroom, bathroom, size'''
    raw_bed_bath_size = zillow_dom_tree.xpath(BED_BATH_SIZE_XPATH)
    bedroom = 0
    bathroom = 0
    size = 0
    bed_bath_size = []
    if(len(raw_bed_bath_size) > 0):
        for item in raw_bed_bath_size:
            if item[0].isdigit():
                bed_bath_size.append(int(re.sub("\D", "", item)))
        bedroom = bed_bath_size[0]
        bathroom = bed_bath_size[1]
        size = bed_bath_size[2]

    '''type'''
    property_type = zillow_dom_tree.xpath(TYPE_XPATH)

    if(len(property_type) > 0):
        property_type = property_type[0]
    else:
        property_type = ''

    '''latitude, longitude'''
    geo_json = zillow_dom_tree.xpath(LAT_LONG_XPATH)
    if(len(geo_json) > 0):
        geo_json = json.loads(geo_json[0])
        geo = geo_json["geo"]
        latitude = geo["latitude"]
        longitude = geo["longitude"]
    else:
        latitude = ''
        longitude = ''

    print('test')
    print(latitude)
    print(longitude)

    data = {
        'description': description,
        'bedroom': bedroom,
        'bathroom': bathroom,
        'size': size,
        'img_url': img_url,
        'address': address,
        'street_address': street_address,
        'city': city,
        'state': state,
        'zipcode': zipcode
    }
    return data
