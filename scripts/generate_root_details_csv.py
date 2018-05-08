# -*- coding: utf-8 -*-

# Note: this file should be run after
#     1. generate_metadata_mapping.py is run
#     2. And root_statistics.json is saved to its original location: content/metadata/root_statistics.json

import sys
import json
import csv
import collections


bw_to_ar_map = {
    "A": "ا",
    "b": "ب",
    "t": "ت",
    "v": "ث",
    "j": "ج",
    "H": "ح",
    "x": "خ",
    "d": "د",
    "*": "ذ",
    "r": "ر",
    "z": "ز",
    "s": "س",
    "$": "ش",
    "S": "ص",
    "D": "ض",
    "T": "ط",
    "Z": "ظ",
    "E": "ع",
    "g": "غ",
    "f": "ف",
    "q": "ق",
    "k": "ك",
    "l": "ل",
    "m": "م",
    "n": "ن",
    "h": "ه",
    "w": "و",
    "y": "ي",
    "p": "ة", #teh marbuta

    # "a": '\u064E', # fatha
    # "u": '\u064f', # damma
    # "i": '\u0650', # kasra
    # "F": '\u064B', # fathatayn
    # "N": '\u064C', # dammatayn
    # "K": '\u064D', # kasratayn
    # "~": '\u0651', # shadda
    # "o": '\u0652', # sukun
    #
    # "'": '\u0621', # lone hamza
    # ">": '\u0623', # hamza on alif
    # "<": '\u0625', # hamza below alif
    # "&": '\u0624', # hamza on wa
    # "}": '\u0626', # hamza on ya
    #
    # "|": '\u0622', # madda on alif
    # "{": '\u0671', # alif al-wasla
    # "`": '\u0670', # dagger alif
    # "Y": '\u0649', # alif maqsura

    " ": " "
}

def bw_to_arabic(root):

    result = ""

    for c in root:
        result = result + bw_to_ar_map[c]

    return result.decode("utf-8")


def load_json_from_file(file_name):
    data = None

    with open(file_name) as json_data:
        data = json.load(json_data)

    return data

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

def get_record(root, root_details, meaning_v1_content):

    meaning = ""

    if root in meaning_v1_content:
        meaning = meaning_v1_content[root]

    response = {
        "bw_root": root,
        "root": bw_to_arabic(root).encode("utf-8"),
        "cardinality": root_details['cardinality'],
        "distinct-cardinality": root_details['appears_number_of_surah'],
        "meaning_v1": meaning
    }

    # print(unicode(response))
    return response

if __name__ == '__main__':
    # if len(sys.argv) != 2:
    #     print("Usage: python generate_root_details.py ")
    #     sys.exit(1)

    content = load_json_from_file("../content/metadata/root_statistics.json")
    meaning_v1_content = load_kvp_from_file("../content/translations/english-meaning-v2.txt")

    # rows =
    with open("./root_details.csv", "wb") as file_handle:
        headers = ["root", "bw_root", "cardinality", "distinct-cardinality", "meaning_v1"]
        writer = csv.DictWriter(file_handle, fieldnames=headers)

        for root in content:
            writer.writerow(get_record(root, content[root], meaning_v1_content))

    print("Completed.")
