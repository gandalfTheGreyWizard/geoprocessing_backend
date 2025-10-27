import pymongo
from dotenv import dotenv_values
import json

config = dotenv_values()

mongo_connection_string = "mongodb://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}".format(USERNAME=config['MONGO_DB_USER'], PASSWORD=config['MONGO_DB_PASSWORD'], HOSTNAME=config['MONGO_DB_HOST'], PORT=config['MONGO_DB_PORT'])
client = pymongo.MongoClient(mongo_connection_string)
db = client.get_database(config['MONGO_DB_NAME'])
shapeCollection = db['shapes']

def geo_within_l3_in_l1():
    l1_shape = shapeCollection.find_one({"shapeID": "1811400B80305611676067"})
    query = {
        "level": "l3",
        "geometry": {
            "$geoIntersects": {
                "$geometry": l1_shape['geometry']
                }
            }
        }
    # print(query)
    l3_shapes = shapeCollection.find(query)
    jsonOutput = {}
    jsonOutput['type'] = "FeatureCollection"
    jsonOutput['features'] = []
    for each_geowithin_shape in l3_shapes:
        del each_geowithin_shape['_id']
        jsonOutput['features'].append(each_geowithin_shape)

    print(json.dumps(jsonOutput))

geo_within_l3_in_l1()

