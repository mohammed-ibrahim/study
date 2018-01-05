import collections
import json
from ml_util import get_number_in_arabic

def load_kvp_from_file(file_name):
    data = collections.OrderedDict()

    with open(file_name) as file_pointer:
        line = file_pointer.readline()

        while line:
            parts = line.split("|")

            if len(parts) == 2:
                if len(parts[1].strip()) > 0:
                    data[parts[0]] = parts[1]

            line = file_pointer.readline()

    return data

def load_from_file(file_name, language):
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
            #data[key] = content[2] + get_ayah_number(ayah_number, language).encode('utf8')
            line = file_pointer.readline()

    return data

def get_ayah_number(ayah_number, language):
    if language == 'en':
        return "(" + ayah_number + ")"

    if language == 'ar' or language == 'ur':
        return "(" + get_number_in_arabic(ayah_number) + ")"

    raise Exception('Language: ' + language + ' is not supported for numeric translation')

def load_json_from_file(file_name):
    data = None

    with open(file_name) as json_data:
        data = json.load(json_data)

    return data
