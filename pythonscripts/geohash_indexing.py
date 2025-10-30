import pygeohash as pgh
import numpy as np

from shapely import Polygon,MultiPolygon
from shapely.geometry import shape
import pymongo
from dotenv import dotenv_values
import json
import math

config=dotenv_values()

converted_arr = []
def convert_to_tuples(arr):
    try:
        if (len(arr) == 1):
            for each_arr in arr:
                print('inside if')
        else:
            for each_arr in arr:
                # print(len(each_arr))
                convert_to_tuples(each_arr)
    except Exception as e:
        print(type(arr))
        print(e)
    # new_arr = np.array(arr)
    # print(new_arr.shape)
mongo_connection_string = "mongodb://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}".format(USERNAME=config['MONGO_DB_USER'], PASSWORD=config['MONGO_DB_PASSWORD'], HOSTNAME=config['MONGO_DB_HOST'], PORT=config['MONGO_DB_PORT'])
client = pymongo.MongoClient(mongo_connection_string)
db = client.get_database(config['MONGO_DB_NAME'])

shapeCollection = db['shapes']
hashesCollection = db['geohashes']

def get_geohasahes():
    for index,each_object in enumerate(shapeCollection.find({"level": "l1"})):
        if index == 0:
            shapely_object = shape(each_object['geometry'])
            (min_lat, min_long, max_lat, max_long) = shapely_object.bounds
            bbox = pgh.BoundingBox(min_lat, min_long, max_lat, max_long)
            geohashes_in_bbox = pgh.geohashes_in_box(bbox, precision=7)
            # hashes_feature_collection = {}
            # hashes_feature_collection['type'] = "FeatureCollection"
            # hashes_feature_collection['features'] = []
            iterations = math.floor(len(geohashes_in_bbox) / 1000)
            for i in range(0, iterations):
                geohash_dictionary_objects = []
                lower_bound = (1000 * i) + 1
                upperbound = 1000 * (i + 1)
                if i == iterations:
                    upperbound = len(geohashes_in_bbox) % 1000
                for each_geohash in geohashes_in_bbox[lower_bound: upperbound]:
                    temp_dict = {}
                    temp_dict['hash_id'] = each_geohash
                    temp_dict['type'] = "Feature"
                    temp_dict['geometry'] = {}
                    temp_dict['geometry']['type'] = "Point"
                    (temp_lat, temp_long) = pgh.decode(each_geohash)
                    temp_dict['geometry']['coordinates'] = [temp_lat, temp_long]
                    geohash_dictionary_objects.append(temp_dict)
                    # hashes_feature_collection['features'].append(temp_dict)
                hashesCollection.insert_many(geohash_dictionary_objects)
            # with open('../data/geohashes_test_out.json', 'w') as file:
                # json.dump(hashes_feature_collection, file)
            # print(shapely_object.bounds)
        # convert_to_tuples(shape['geometry']['coordinates'])
        # for coordinates_arr in shape['geometry']['coordinates']:
            # print(coordinates_arr)
            # print("\n")
get_geohasahes()

