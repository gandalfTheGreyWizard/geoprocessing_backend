import shapefile
import os

sf = shapefile.Reader(os.path.join(os.getcwd(), '../data/geoBoundaries-IND-ADM1.shp'))
print(sf)

records = sf.records()
fields = sf.fields
print(fields)
shapes_arr = []
# for each_shape in sf.shapes():
    # print(each_shape.record())
    # shapes_arr.append(each_shape.__geo_interface__['properties'])
# for each_shape in shapes_arr:
    # print(each_shape)
    # print('\n')
# for each_record in sf.records():
    # print(each_record.as_dict())
    # print('uid', each_record.oid)
    # print(sf.shape(each_record.oid))


def convert_to_geojson():
    master_temp_feature_collection = {}
    master_temp_feature_collection['type'] = "FeatureCollection"
    master_temp_feature_collection['features'] = []
    for index, each_record in enumerate(sf.records()):
        temp_dict = {}
        temp_dict['type'] = 'Feature'
        temp_dict['properties'] = each_record.as_dict()
        temp_dict['geometry'] = sf.shape(each_record.oid).__geo_interface__
        if index == 0:
            print(temp_dict)

convert_to_geojson()
# for each_shape_record in sf.shapeRecords():
    # print(each_shape_record.)
