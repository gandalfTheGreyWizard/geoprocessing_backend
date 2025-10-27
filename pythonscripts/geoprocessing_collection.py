import shapefile
import os
import json
import pymongo
from argparse import ArgumentParser
from dotenv import dotenv_values

config=dotenv_values()

mongo_connection_string = "mongodb://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}".format(USERNAME=config['MONGO_DB_USER'], PASSWORD=config['MONGO_DB_PASSWORD'], HOSTNAME=config['MONGO_DB_HOST'], PORT=config['MONGO_DB_PORT'])
print(mongo_connection_string)
client = pymongo.MongoClient(mongo_connection_string)
db = client.get_database(config['MONGO_DB_NAME'])

parser = ArgumentParser(
        prog="lingo",
        description="A script to process shapefiles and index them to mongodb",
        )

parser.add_argument('-i', '--index', help='function to trigger while running the script')
args = parser.parse_args()

shapeCollection = db['shapes']

# function definitions
def index_l1():
    sf = shapefile.Reader(os.path.join(os.getcwd(), '../data/geoBoundaries-IND-ADM1.shp'))
    master_temp_feature_collection = {}
    master_temp_feature_collection['type'] = "FeatureCollection"
    master_temp_feature_collection['features'] = []
    for index, each_record in enumerate(sf.records()):
        # print('record is ', each_record.as_dict())
        temp_dict = {}
        temp_dict['type'] = 'Feature'
        temp_dict['properties'] = each_record.as_dict()
        temp_dict['name'] = temp_dict['properties']['shapeName']
        temp_dict['shapeID'] = temp_dict['properties']['shapeID']
        temp_dict['level'] = 'l1'
        temp_dict['geometry'] = sf.shape(each_record.oid).__geo_interface__
        # print(temp_dict)
        filterCollection = {}
        filterCollection['shapeID'] = temp_dict['shapeID']
        print('filter is ', filterCollection)
        try:
            shapeCollection.update_one(filterCollection, {'$set': temp_dict}, upsert=True)
        except Exception as e:
            print(e)
    # print(json.dumps(master_temp_feature_collection))
    sf.close()

def index_l2():
    sf = shapefile.Reader(os.path.join(os.getcwd(), '../data/geoBoundaries-IND-ADM2.shp'))
    master_temp_feature_collection = {}
    master_temp_feature_collection['type'] = "FeatureCollection"
    master_temp_feature_collection['features'] = []
    # collection = db.get_collection('shapes')
    for index, each_record in enumerate(sf.records()):
        temp_dict = {}
        temp_dict['type'] = 'Feature'
        temp_dict['properties'] = each_record.as_dict()
        temp_dict['name'] = temp_dict['properties']['shapeName']
        temp_dict['shapeID'] = temp_dict['properties']['shapeID']
        temp_dict['level'] = 'l2'
        temp_dict['geometry'] = sf.shape(each_record.oid).__geo_interface__
        # print(temp_dict)
        filterCollection = {}
        filterCollection['shapeID'] = temp_dict['shapeID']
        print('filter is ', filterCollection)
        try:
            shapeCollection.update_one(filterCollection, {'$set': temp_dict}, upsert=True)
        except Exception as e:
            print(e)
        # print(temp_dict)
        # collection.insert_one(temp_dict)
    # print(json.dumps(master_temp_feature_collection))


def index_l3():
    sf = shapefile.Reader(os.path.join(os.getcwd(), '../data/geoBoundaries-IND-ADM3.shp'))
    master_temp_feature_collection = {}
    master_temp_feature_collection['type'] = "FeatureCollection"
    master_temp_feature_collection['features'] = []
    # collection = db.get_collection('shapes')
    for index, each_record in enumerate(sf.records()):
        temp_dict = {}
        temp_dict['type'] = 'Feature'
        temp_dict['properties'] = each_record.as_dict()
        temp_dict['name'] = temp_dict['properties']['shapeName']
        temp_dict['shapeID'] = temp_dict['properties']['shapeID']
        temp_dict['level'] = 'l3'
        temp_dict['geometry'] = sf.shape(each_record.oid).__geo_interface__
        # print(temp_dict)
        filterCollection = {}
        filterCollection['shapeID'] = temp_dict['shapeID']
        print('filter is ', filterCollection)
        try:
            shapeCollection.update_one(filterCollection, {'$set': temp_dict}, upsert=True)
        except Exception as e:
            print(e)
    print(json.dumps(master_temp_feature_collection))

def index_l4():
    sf = shapefile.Reader(os.path.join(os.getcwd(), '../data/geoBoundaries-IND-ADM4.shp'))
    master_temp_feature_collection = {}
    master_temp_feature_collection['type'] = "FeatureCollection"
    master_temp_feature_collection['features'] = []
    for index, each_record in enumerate(sf.records()):
        temp_dict = {}
        temp_dict['type'] = 'Feature'
        temp_dict['properties'] = each_record.as_dict()
        temp_dict['name'] = temp_dict['properties']['shapeName']
        temp_dict['shapeID'] = temp_dict['properties']['shapeID']
        temp_dict['level'] = 'l4'
        temp_dict['geometry'] = sf.shape(each_record.oid).__geo_interface__
        # print(temp_dict)
        filterCollection = {}
        filterCollection['shapeID'] = temp_dict['shapeID']
        print('filter is ', filterCollection)
        try:
            shapeCollection.update_one(filterCollection, {'$set': temp_dict}, upsert=True)
        except Exception as e:
            print(e)

def index_l5():
    sf = shapefile.Reader(os.path.join(os.getcwd(), '../data/geoBoundaries-IND-ADM5.shp'))
    master_temp_feature_collection = {}
    master_temp_feature_collection['type'] = "FeatureCollection"
    master_temp_feature_collection['features'] = []
    for index, each_record in enumerate(sf.records()):
        temp_dict = {}
        temp_dict['type'] = 'Feature'
        temp_dict['properties'] = each_record.as_dict()
        temp_dict['name'] = temp_dict['properties']['shapeName']
        temp_dict['shapeID'] = temp_dict['properties']['shapeID']
        temp_dict['level'] = 'l5'
        temp_dict['geometry'] = sf.shape(each_record.oid).__geo_interface__
        # print(temp_dict)
        filterCollection = {}
        filterCollection['shapeID'] = temp_dict['shapeID']
        print('filter is ', filterCollection)
        try:
            shapeCollection.update_one(filterCollection, {'$set': temp_dict}, upsert=True)
        except Exception as e:
            print(e)

def convert_to_geojson():
    master_temp_feature_collection = {}
    master_temp_feature_collection['type'] = "FeatureCollection"
    master_temp_feature_collection['features'] = []
    for index, each_record in enumerate(sf.records()):
        # print('record is ', each_record.as_dict())
        temp_dict = {}
        # temp_dict['id'] = each_record['shapeId']
        temp_dict['type'] = 'Feature'
        temp_dict['properties'] = each_record.as_dict()
        temp_dict['geometry'] = sf.shape(each_record.oid).__geo_interface__

        # if index == 0:
            # print(temp_dict['properties'])
        # print(temp_dict['properties']['shapeName'])
        # collection.insert_one(temp_dict)
        # master_temp_feature_collection['features'].append(temp_dict)
    # print(json.dumps(master_temp_feature_collection))

# parser arguments handling
if args.index == 'l1':
    index_l1()
elif args.index == 'l2':
    index_l2()
elif args.index == 'l3':
    index_l3()
elif args.index == 'l4':
    index_l4()
elif args.index == 'l5':
    index_l5()
else:
    print("please use the index flag to choose an indexing method")
