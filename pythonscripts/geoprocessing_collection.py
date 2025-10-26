import shapefile
import os
import json
import pymongo
from argparse import ArgumentParser

client = pymongo.MongoClient("mongodb://root:example@localhost:27017")
db = client.get_database("testIndexing")

parser = ArgumentParser(
        prog="lingo",
        description="A script to process shapefiles and index them to mongodb",
        )

parser.add_argument('-i', '--index', help='function to trigger while running the script')
args = parser.parse_args()

# function definitions
def index_l1():
    sf = shapefile.Reader(os.path.join(os.getcwd(), '../data/geoBoundaries-IND-ADM1.shp'))
    master_temp_feature_collection = {}
    master_temp_feature_collection['type'] = "FeatureCollection"
    master_temp_feature_collection['features'] = []
    collection = db.get_collection("shapes")
    for index, each_record in enumerate(sf.records()):
        # print('record is ', each_record.as_dict())
        temp_dict = {}
        temp_dict['type'] = 'feature'
        temp_dict['properties'] = each_record.as_dict()
        temp_dict['name'] = temp_dict['properties']['shapeName']
        temp_dict['level'] = 'l1'
        temp_dict['geometry'] = sf.shape(each_record.oid).__geo_interface__
        print(temp_dict)
        collection.insert_one(temp_dict)
    sf.close()

def index_l2():
    sf = shapefile.Reader(os.path.join(os.getcwd(), '../data/geoBoundaries-IND-ADM2.shp'))
    master_temp_feature_collection = {}
    master_temp_feature_collection['type'] = "FeatureCollection"
    master_temp_feature_collection['features'] = []
    collection = db.get_collection('shapes')
    for index, each_record in enumerate(sf.records()):
        temp_dict = {}
        temp_dict['type'] = 'feature'
        temp_dict['properties'] = each_record.as_dict()
        temp_dict['name'] = temp_dict['properties']['shapeName']
        temp_dict['level'] = 'l2'
        temp_dict['geometry'] = sf.shape(each_record.oid).__geo_interface__
        print(temp_dict)
        collection.insert_one(temp_dict)
    print(json.dumps(master_temp_feature_collection))


def index_l3():
    sf = shapefile.Reader(os.path.join(os.getcwd(), '../data/geoBoundaries-IND-ADM3.shp'))
    master_temp_feature_collection = {}
    master_temp_feature_collection['type'] = "FeatureCollection"
    master_temp_feature_collection['features'] = []
    collection = db.get_collection('shapes')
    for index, each_record in enumerate(sf.records()):
        temp_dict = {}
        temp_dict['type'] = 'feature'
        temp_dict['properties'] = each_record.as_dict()
        temp_dict['name'] = temp_dict['properties']['shapeName']
        temp_dict['level'] = 'l3'
        temp_dict['geometry'] = sf.shape(each_record.oid).__geo_interface__
        collection.insert_one(temp_dict)
    # print(json.dumps(master_temp_feature_collection))

def process_shapefile():
    sf = shapefile.Reader(os.path.join(os.getcwd(), '../data/geoBoundaries-IND-ADM4.shp'))
    master_temp_feature_collection = {}
    master_temp_feature_collection['type'] = "FeatureCollection"
    master_temp_feature_collection['features'] = []
    for index, each_record in enumerate(sf.records()):
        temp_dict = {}
        temp_dict['type'] = 'Feature'
        temp_dict['properties'] = each_record.as_dict()
        temp_dict['geometry'] = sf.shape(each_record.oid).__geo_interface__
        master_temp_feature_collection['features'].append(temp_dict)
    print(json.dumps(master_temp_feature_collection))

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
elif args.index == 'current':
    process_shapefile()
else:
    print("please use the index flag to choose an indexing method")
