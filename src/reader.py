import collections
import json

def load_from_file(file_name):
    data = collections.OrderedDict()

    with open(file_name) as file_pointer:
        line = file_pointer.readline()

        while line:
            if not line:
                line = file_pointer.readline()
                continue

            if not line[0].isdigit():
                line = file_pointer.readline()
                continue

            content = line.split("|")
            surah_number = content[0]
            ayah_number = content[1]

            key = surah_number + ":" + ayah_number
            data[key] = content[2]
            line = file_pointer.readline()

    return data

def load_json_from_file(file_name):
    data = None

    with open(file_name) as json_data:
        data = json.load(json_data)

    return data
