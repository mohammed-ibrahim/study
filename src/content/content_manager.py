
def get_ruku_content(app_data, ruku_number):
    result = app_data.get_surah_and_ruku_metadata(ruku_number)
    surah_data = result["surah_data"]
    ruku_data = result["ruku_data"]

    aayaah = list()
    roots = set()
    for ayah_number in ruku_data["aayaah_in_ruku"]:
        ayah_details = get_ayah_details(app_data, ayah_number)
        aayaah.append(ayah_details)

        for root in ayah_details["root_sequence"]:
            roots.add(root)

    data = {
        "surah_name": surah_data["name"],
        "surah_number": result["surah_number"],
        "ruku_number": ruku_number,
        "current_ruku_in_surah": result["current_ruku_in_surah"],
        "number_of_ruku_in_surah": len(surah_data["ruku"]),
        "next_ruku_number": get_next_ruku_number(app_data, ruku_number),
        "previous_ruku_number": get_previous_ruku_number(app_data, ruku_number),
        "juz_number": "PENDING",
        "ayah_number_sequence": ruku_data["aayaah_in_ruku"],
        "aayaah": aayaah,
        "translation_sequence": app_data.translation_sequence,
        "root_details": get_root_details(app_data, roots)
    }

    return data

def get_next_ruku_number(app_data, ruku_number):
    if (str(ruku_number + 1)) in app_data.ruku_to_surah_mapping:
        return (ruku_number + 1)

    return 1

def get_previous_ruku_number(app_data, ruku_number):
    if ruku_number <= 1:
        return 556

    str_prev_number = str(ruku_number - 1)
    if str_prev_number in app_data.ruku_to_surah_mapping:
        return int(str_prev_number)

    return 556

def get_ayah_details(app_data, ayah_number):
    ayah_details = {
        "ayah_number": ayah_number,
        "arabic_content": {
            "uthmani": app_data.arabic[str(ayah_number)]
        },
        "translations": {

        }
    }

    ayah_details["translations"]["translation_yusuf_ali"] = app_data.translation_yusuf_ali.get_ayah_and_details(ayah_number)
    ayah_details["translations"]["translation_shakir"] = app_data.translation_shakir.get_ayah_and_details(ayah_number)
    ayah_details["translations"]["translation_maulana_maududi"] = app_data.translation_maulana_maududi.get_ayah_and_details(ayah_number)
    ayah_details["translations"]["translation_maulana_jalandhry"] = app_data.translation_maulana_jalandhry.get_ayah_and_details(ayah_number)

    str_ayah_number = str(ayah_number)
    if str_ayah_number in app_data.verse_number_to_root_sequence_mapping:
        ayah_details["root_sequence"] = app_data.verse_number_to_root_sequence_mapping[str_ayah_number]
        ayah_details["detailed_root_sequence"] = build_detailed_root_sequence(app_data, app_data.verse_number_to_root_sequence_mapping[str_ayah_number])
    else:
        ayah_details["root_sequence"] = list()

    return ayah_details

def build_detailed_root_sequence(app_data, root_sequence):
    content = []

    for root in root_sequence:
        content.append(get_root_details_by_root(root, app_data))

    return content

def get_root_details_by_root(root, app_data):
    english_meaning = "PENDING"
    urdu_meaning = "PENDING"

    if root in app_data.root_meaning and 'eng' in app_data.root_meaning[root]:
        english_meaning = app_data.root_meaning[root]['eng']

    if root in app_data.root_meaning and 'urdu' in app_data.root_meaning[root]:
        urdu_meaning = app_data.root_meaning[root]['urdu']

    response = {
        "bw_root": root,
        "statistics": {
            "num_of_occurrence": app_data.root_statistics[root]["cardinality"],
            "appears_number_of_surah": app_data.root_statistics[root]["appears_number_of_surah"]
        },
        "english-meaning": unicode(english_meaning, errors='ignore'),
        "urdu-meaning": unicode(urdu_meaning, errors='ignore')
    }

    return response

def get_root_details(app_data, roots):
    response = {}

    for root in roots:
        english_meaning = "PENDING"
        urdu_meaning = "PENDING"

        if root in app_data.root_meaning and 'eng' in app_data.root_meaning[root]:
            english_meaning = app_data.root_meaning[root]['eng']

        if root in app_data.root_meaning and 'urdu' in app_data.root_meaning[root]:
            urdu_meaning = app_data.root_meaning[root]['urdu']

        response[root] = {
            "statistics": {
                "num_of_occurrence": app_data.root_statistics[root]["cardinality"],
                "appears_number_of_surah": app_data.root_statistics[root]["appears_number_of_surah"]
            },
            "english-meaning": unicode(english_meaning, errors='ignore'),
            "urdu-meaning": unicode(urdu_meaning, errors='ignore')
        }

    return response
