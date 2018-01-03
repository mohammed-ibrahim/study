import collections
import json

def load_from_file(file_name):
    data = collections.OrderedDict()

    with open(file_name) as file_pointer:
        line = file_pointer.readline()
        content = line.split("|")
        surah_number = content[0]
        ayah_number = content[1]

        key = surah_number + ":" + ayah_number
        data[key] = content[2]

    return data

def load_json_from_file(file_name):
    data = None

    with open(file_name) as json_data:
        data = json.load(json_data)

    return data
