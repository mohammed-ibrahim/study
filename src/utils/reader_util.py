import collections
import json
import csv
from src.utils import ml_util

def load_root_meaning(file_name):
    root_meaning = {}
    n_urdu = 0
    n_eng = 0
    n_rows = 0

    with open(file_name, 'rb') as file_pointer:
        reader = csv.reader(file_pointer)
        headers = None

        for row in reader:
            n_rows += 1

            if headers is None:
                headers = row
            else:
                bw_root = row[1]
                urdu_meaning = row[7].strip()
                eng_meaning = row[8].strip()

                if len(urdu_meaning) > 0 or len(eng_meaning) > 0:
                    root_meaning[bw_root] = {}

                    if len(urdu_meaning) > 0:
                        root_meaning[bw_root]['urdu'] = urdu_meaning
                        # print("urdu: %s" % urdu_meaning)
                        n_urdu += 1

                    if len(eng_meaning) > 0:
                        root_meaning[bw_root]['eng'] = eng_meaning
                        # print("eng: %s" % eng_meaning)
                        n_eng += 1

    print("Total rows: %s, Total urdu: %d, Totan eng: %d" % (n_rows, n_urdu, n_eng))
    return root_meaning

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
        return "(" + ml_util.get_number_in_arabic(ayah_number) + ")"

    raise Exception('Language: ' + language + ' is not supported for numeric translation')

def load_json_from_file(file_name):
    data = None

    with open(file_name) as json_data:
        data = json.load(json_data)

    return data
